from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from accounts.forms import UserCreationForm, LoginForm


class RegisterView(CreateView):
    model = User
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")
    form_class = UserCreationForm

    # def post(self, request, *args, **kwargs):
    #     pass


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("home")
    form_class = LoginForm
