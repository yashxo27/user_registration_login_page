from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from kapp1.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser