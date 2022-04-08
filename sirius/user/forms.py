from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class AccountSignupForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    class Meta:
        model = get_user_model()
        fields = [
            'username',
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
        model = get_user_model()
        fields = [
            'email',
            'password',
        ]
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login credentials!")

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
        ]
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            get_user_model().objects.exclude(pk=self.instance.pk).get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % email)
