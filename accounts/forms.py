# /notekeeper/accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Organization

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class OrganizationRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Organization
        fields = ('name',)

    def save_user(self, commit=True):
        user_data = {
            'username': self.cleaned_data['username'],
            'email': self.cleaned_data['email'],
        }
        user = User(**user_data)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data