from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=50)
    birthday = models.DateField()
    company_user = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'pk': self.pk})

    def is_company_user(self):
        return self.company_user


