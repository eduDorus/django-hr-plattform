from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    company_account = forms.BooleanField()
    birthday = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'company_account', 'birthday']
