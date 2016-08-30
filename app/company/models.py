from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    SIZE = (
        (10, '1 - 10'),
        (50, '11 - 50'),
        (100, '51 - 100'),
        (250, '101 - 250'),
        (500, '251 - 500'),
        (1000, '501 - 1000'),
        (10000, '1000 - 10000'),
        (100000, '10000 +'),
    )

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    size = models.IntegerField(choices=SIZE, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=None, null=True, blank=True)
    website = models.URLField(max_length=250, null=True, blank=True)
    admins = models.ManyToManyField(User, related_name='admins')
    permission_requests = models.ManyToManyField(User, related_name='permission_requests')

    def get_absolute_url(self):
        return reverse('company:company-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
