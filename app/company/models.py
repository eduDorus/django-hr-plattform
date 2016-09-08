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
    description = models.TextField(null=True, blank=True, max_length=1500)
    size = models.IntegerField(choices=SIZE, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=None, null=True, blank=True)
    website = models.URLField(max_length=250, null=True, blank=True)
    permission_requests = models.ManyToManyField(User, related_name='permission_requests')

    def get_absolute_url(self):
        return reverse('company-profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.degree


class Job(models.Model):
    TEN_PERCENT = 10
    TWENTY_PERCENT = 20
    THIRTY_PERCENT = 30
    FORTY_PERCENT = 40
    FIFTY_PERCENT = 50
    SIXTY_PERCENT = 60
    SEVENTY_PERCENT = 70
    EIGHTY_PERCENT = 80
    NINETY_PERCENT = 90
    HUNDRED_PERCENT = 100

    EMPLOYMENT_GRADE = (
        (TEN_PERCENT, '10 %'),
        (TWENTY_PERCENT, '20 %'),
        (THIRTY_PERCENT, '30 %'),
        (FORTY_PERCENT, '40 %'),
        (FIFTY_PERCENT, '50 %'),
        (SIXTY_PERCENT, '60 %'),
        (SEVENTY_PERCENT, '70 %'),
        (EIGHTY_PERCENT, '80 %'),
        (NINETY_PERCENT, '90 %'),
        (HUNDRED_PERCENT, '100 %'),
    )

    company = models.ForeignKey(Company, on_delete=None)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1500)
    employment_grade = models.PositiveIntegerField(choices=EMPLOYMENT_GRADE)

    min_degree = models.ForeignKey(Education, on_delete=None)

    # Softskills
    office = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('company-job-list', kwargs={'pk': 1})


class Skill(models.Model):
    job = models.ForeignKey(Job, on_delete=None)
    name = models.CharField(max_length=100)
    experience = models.PositiveSmallIntegerField()
    level = models.PositiveSmallIntegerField()
