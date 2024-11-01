from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import GarbageReport, GarbageAdmin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .forms import UserRegistrationForm, GarbageAdminRegistrationForm, GarbageReportForm
from .models import UserProfile, GarbageAdmin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json

def test(request):
    return render(request, 'core/landing.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile.objects.get(user=user)
            
            # Send verification email
            html_message = render_to_string('core/email/verify_email.html', {
                'user': user,
                'token': profile.verification_token
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                'Verify your email',
                plain_message,
                settings.EMAIL_HOST_USER,
                [user.email],
                html_message=html_message
            )
            
            messages.success(request, 'Registration successful. Please check your email to verify your account.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register_user.html', {'form': form})

def verify_email(request, token):
    try:
        profile = UserProfile.objects.get(verification_token=token)
        profile.is_verified = True
        profile.verification_token = None
        profile.save()
        messages.success(request, 'Email verified successfully. You can now login.')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Invalid verification token.')
    return redirect('login')

@login_required
def register_garbage_admin(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('home')
        
    if request.method == 'POST':
        form = GarbageAdminRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            garbage_admin, password = form.save()
            
            # Send credentials email
            html_message = render_to_string('core/email/admin_credentials.html', {
                'admin': garbage_admin,
                'password': password
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                'Your Garbage Collection Admin Account',
                plain_message,
                settings.EMAIL_HOST_USER,
                [garbage_admin.user.email],
                html_message=html_message
            )
            
            messages.success(request, 'Garbage Admin registered successfully. Credentials have been sent to their email.')
            return redirect('admin_dashboard')
    else:
        form = GarbageAdminRegistrationForm()
    return render(request, 'core/register_garbage_admin.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Check if user is verified (for regular users)
            if hasattr(user, 'userprofile') and not user.userprofile.is_verified:
                messages.error(request, 'Please verify your email before logging in.')
                return redirect('login')
            # Check if admin is authorized (for garbage admins)
            if hasattr(user, 'garbageadmin') and not user.garbageadmin.is_authorized:
                messages.error(request, 'Your admin account is not yet authorized.')
                return redirect('login')
            
            login(request, user)
            if hasattr(user, 'garbageadmin'):
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def user_profile(request):
    user = request.user
    if hasattr(user, 'userprofile'):
        profile = user.userprofile
    elif hasattr(user, 'garbageadmin'):
        profile = user.garbageadmin
    else:
        profile = None

    return render(request, 'core/user_profile.html', {'profile': profile})


def user_logout(request):
    logout(request)
    return redirect('login')

def is_garbage_admin(user):
    return hasattr(user, 'garbageadmin') and user.garbageadmin.is_authorized

@login_required
@user_passes_test(is_garbage_admin)
def admin_dashboard(request):
    admin = request.user.garbageadmin
    reports = GarbageReport.objects.filter(
        city=admin.city,
        status='pending'
    ).order_by('-created_at')
    
    context = {
        'reports': reports,
        'pending_count': reports.filter(status='pending').count(),
        'in_progress_count': reports.filter(status='in_progress').count(),
        'completed_count': reports.filter(status='completed').count(),
    }
    return render(request, 'core/admin_dashboard.html', context)

@login_required
@user_passes_test(is_garbage_admin)
def report_detail(request, report_id):
    report = get_object_or_404(GarbageReport, id=report_id, city=request.user.garbageadmin.city)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            report.status = 'in_progress'
            report.assigned_admin = request.user.garbageadmin
        elif action == 'complete':
            report.status = 'completed'
            
            # Send completion email to user
            html_message = render_to_string('core/email/report_completed.html', {
                'report': report
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                'Garbage Collection Report Completed',
                plain_message,
                settings.EMAIL_HOST_USER,
                [report.user.email],
                html_message=html_message
            )
            
        report.save()
        messages.success(request, f'Report status updated to {report.status}')
        return redirect('admin_dashboard')
    
    return render(request, 'core/report_detail.html', {'report': report})


from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import GarbageReport

@login_required
def user_dashboard(request):
    # Original QuerySet with filters
    reports_queryset = GarbageReport.objects.filter(user=request.user).order_by('-created_at')
    
    # Get the status counts before pagination
    pending_count = reports_queryset.filter(status='pending').count()
    in_progress_count = reports_queryset.filter(status='in_progress').count()
    completed_count = reports_queryset.filter(status='completed').count()
    
    # Pagination
    paginator = Paginator(reports_queryset, 10)
    page = request.GET.get('page')
    reports = paginator.get_page(page)
    
    context = {
        'reports': reports,
        'pending_count': pending_count,
        'in_progress_count': in_progress_count,
        'completed_count': completed_count,
    }
    return render(request, 'core/user_dashboard.html', context)

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = GarbageReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.latitude = request.POST.get('latitude')
            report.longitude = request.POST.get('longitude')
            report.save()
            
            messages.success(request, 'Report submitted successfully!')
            return redirect('user_dashboard')
    else:
        form = GarbageReportForm()
    
    return render(request, 'core/submit_report.html', {'form': form})


