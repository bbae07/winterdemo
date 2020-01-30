from django import forms
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    gender = forms.CharField(max_length=6, required=True, help_text='Enter assigned gender at birth (Male or Female).')

    class Meta:
        model = CustomUser
        fields = ('username', 'gender')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'gender')