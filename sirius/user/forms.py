from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django import forms

class AccountSignupForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = [
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'gender',
        ]

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = [
            'email',
            'password',
        ]
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login credentials!")