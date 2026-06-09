from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # User URLs
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.user_signup, name='user_signup'),
    path('profile/', views.user_profile, name='user_profile'),  # ✅ MUST HAVE
    path('logout/', views.user_logout, name='user_logout'),
    
    # Donor URLs
    path('donor-register/', views.donor_register, name='donor_register'),
    path('donor-success/', views.donor_success, name='donor_success'),
    
    # Blood Request
    path('blood-request/', views.blood_request, name='blood_request'),
    path('submit-request/', views.submit_request, name='submit_request'),
    
    # Admin
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    
    # Other
    path('about/', views.about, name='about'),
    path('certificate/', views.certificate, name='certificate'),
]