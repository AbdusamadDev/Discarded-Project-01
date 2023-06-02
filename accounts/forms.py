from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        fields = ["username", "email", "password"]
        model = User


class LoginForm(forms.ModelForm):
    class Meta:
        fields = ["email", "password"]
        model = User
