# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),
    path('register-admin/', views.register_garbage_admin, name='register_admin'),
]
urlpatterns += [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path("profile/", views.user_profile, name="profile"),
    # path("edit-profile", views.edit_profile, name="edit_profile"),
    # path("change-password", views.change_password, name="change_password"),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    
]
urlpatterns += [
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('submit-report/', views.submit_report, name='submit_report'),
]
urlpatterns += [
    path("",views.test, name ='test')
]