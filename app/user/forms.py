from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('transgender_m', 'Transgender born as male'),
        ('transgender_f', 'Transgender born as female'),
        ('other', 'other'),
    )

    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=GENDER)
    birthday = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'birthday', 'password']
