from django import forms
from django.contrib.auth.models import User
from .models import Job

from application.models import Process

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


class JobModelForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['created', 'company', 'slug']

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company')
        super(JobModelForm, self).__init__(*args, **kwargs)
        self.fields['applications_process'].queryset = Process.objects.filter(company=company)