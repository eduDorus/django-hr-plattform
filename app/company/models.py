from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

LEVEL = (
    (1, 'The employee knows what it is'),
    (2, 'The employee is a beginner at it'),
    (3, 'The employee Good at it'),
    (4, 'The employee did advanced stuff with it'),
    (5, 'The employee is specialized in it'),
)


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
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True, max_length=1500)
    size = models.IntegerField(choices=SIZE, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=None, null=True, blank=True)
    website = models.URLField(max_length=250, null=True, blank=True)
    permission_requests = models.ManyToManyField(User, related_name='permission_requests', blank=True)

    logo = models.ImageField(upload_to='media/logos', default='media/logos/default-logo.jpg')
    logo_thumbnail = ImageSpecField(source='logo',
                                    processors=[ResizeToFill(150, 150)],
                                    format='JPEG',
                                    options={'quality': 100})

    def get_absolute_url(self):
        return reverse('company-profile', kwargs={'company_slug': self.slug})

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

    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)

    min_degree = models.ForeignKey(Education, on_delete=None)

    applications_process = models.ForeignKey('application.Process', on_delete=None)

    created = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('company-job-detail', kwargs={'company_slug': self.company.slug, 'pk': self.pk})

    def __str__(self):
        return "%s: %s" % (self.company.name, self.title)


class Skill(models.Model):
    job = models.ForeignKey(Job, on_delete=None)
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(choices=LEVEL)

    def __str__(self):
        return self.name


class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=None)
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(choices=LEVEL)

    def __str__(self):
        return self.name


class Preference(models.Model):
    EARNING = (
        (35000, "35'000 - 50'000, (~3500 per month)"),
        (50000, "50'000 - 65'000, (~4800 per month)"),
        (65000, "65'000 - 80'000, (~6000 per month)"),
        (80000, "80'000 - 95'000, (~7300 per month)"),
        (100000, "100'000 - 125'000, (~9400 per month)"),
        (125000, "125'000 - 150'000, (~11'000 per month)"),
    )

    job = models.ForeignKey(Job, on_delete=None)
    earning = models.IntegerField(choices=EARNING)

    def __str__(self):
        return "%s: %s" % (self.job.title, self.earning)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slug = slugify(instance.name)
        print(slug)
        exists = Company.objects.filter(slug=slug).exists()
        if exists:
            slug = "%s-%s" % (slug, instance.id)
        instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Company)
