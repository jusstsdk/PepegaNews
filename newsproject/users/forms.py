from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

User = get_user_model()


class UserCreationForm(UserCreationForm):
    # email = forms.EmailField(
    #     label=_("Email"),
    #     max_length=254,
    #     widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control', 'placeholder': 'Email'})
    # )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "email": EmailInput(attrs={
                'autocomplete': 'email',
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            # "password": PasswordInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Password'
            # })

        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        "class": "form-control",
        "placeholder": "Username"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            })
        }
