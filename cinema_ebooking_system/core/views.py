from django.shortcuts import render
from django.views.generic import View, TemplateView

from core.models import User 

# Create your views here.

class HomeView(TemplateView):
    template_name='core/home.html'

# class UserLoginView():
#     def post(request):   
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             ...
#         else:
#             # Return an 'invalid login' error message.
#             ...

class SignupView(TemplateView):
    template_name='core/signup.html'

class VerifyEmailView(TemplateView):
    template_name='core/verify_email.html'

class LoginEmailView(TemplateView):
    template_name='core/login.html'

class ForgotPasswordView(TemplateView):
    template_name='core/forgot_password.html'