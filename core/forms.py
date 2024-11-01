# core/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, GarbageAdmin, GarbageReport
import random
import string

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                verification_token=''.join(random.choices(string.ascii_letters + string.digits, k=32))
            )
        return user

class GarbageAdminRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = GarbageAdmin
        fields = ['phone_number', 'city', 'id_card_image', 'profile_image']
    
    def save(self, commit=True):
        # Generate random password
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        
        # Create User instance
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=password,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        
        # Create GarbageAdmin instance
        garbage_admin = super().save(commit=False)
        garbage_admin.user = user
        if commit:
            garbage_admin.save()
        
        return garbage_admin, password
    
class GarbageReportForm(forms.ModelForm):
    class Meta:
        model = GarbageReport
        fields = ['image', 'description', 'address', 'city']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }