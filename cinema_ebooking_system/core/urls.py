from django.urls import path
from . import views

urlpatterns = [
     
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginEmailView.as_view(), name='login'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('verify_email', views.VerifyEmailView.as_view(), name='verify_email'),
    path('forgot_password', views.ForgotPasswordView.as_view(), name='forgot_password'),
]
