from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Enter your Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input', 
            'placeholder': 'Enter Username', 
            'style': 'width:250px; font-size: 16px; color: green;width:200px'
        }),
        max_length=150  # Django allows up to 150 characters for username
    )
    
    password1 = forms.CharField(
        label="Create Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Create Password',
            'style': 'font-size: 16px; color: red; width:200px'
        })
    )
    
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Confirm Password',
            'style': 'font-size: 16px; color: red; width:200px'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
