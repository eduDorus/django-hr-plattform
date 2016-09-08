from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=50)
    birthday = models.DateField()
    company = models.ForeignKey('company.Company', on_delete=None, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'pk': self.pk})

    def is_company_user(self):
        return self.company is not None

    def get_company_id(self):
        if self.company is not None:
            return self.company.id
