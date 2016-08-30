from django import forms
from django.contrib.auth.models import User


class CompanyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    company_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'company_name']
