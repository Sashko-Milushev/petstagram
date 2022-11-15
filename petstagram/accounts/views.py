from django.shortcuts import render
from django.contrib.auth import views as auth_views


# def login_user(request):
#     return render(request, 'accounts/login-page.html')

class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'

def register_user(request):
    return render(request, 'accounts/register-page.html')


def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
