from django import forms
from django.contrib.auth.models import User


class CompanyUserForm(forms.ModelForm):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('transgender_m', 'Transgender born as male'),
        ('transgender_f', 'Transgender born as female'),
        ('other', 'other'),
    )

    password = forms.CharField(widget=forms.PasswordInput)
    company_name = forms.CharField(max_length=100)

    gender = forms.ChoiceField(choices=GENDER)
    birthday = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'gender', 'first_name', 'last_name', 'birthday', 'email', 'password', 'company_name']
