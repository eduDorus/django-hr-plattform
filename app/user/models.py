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


class Education(models.Model):
    ACADEMIC_LEVEL = (
        ('Msc', 'Masters'),
        ('Bsc', 'Bachelor'),
        ('HF', 'Höhere Fachschule'),
        ('EFZ', 'Eidgenösisches Fähigkeits Zeugnis'),
        # TODO add Academic levels, to go international we need a table for this
    )

    user = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100, choices=ACADEMIC_LEVEL)
    specialization = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    # location = models.ForeignKey(Location) # TODO Add location
    graduate_year = models.DateField()

    def get_absolute_url(self):
        return reverse('user-cv-index')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-graduate_year']


class Experience(models.Model):
    POSITION = (
        ('responsible', 'Employee with responsibilities'),
        ('leader', 'Team leader'),
        # TODO add positions here
    )

    EMPLOYMENT_TYPE = (
        ('fulltime', 'Fulltime'),
        ('parttime', 'Parttime'),
        ('freelancer', 'Freelancer'),
        # TODO add employment-types here
    )

    user = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=POSITION)
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT_TYPE)
    employer = models.CharField(
        max_length=100)  # TODO Is it possible to extract all employers from the swiss trade register
    # sector = models.ForeignKey(Sector) # TODO add employment-types here
    # location = models.ForeignKey(Location) # TODO Add location
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse('user-cv-index')

    class Meta:
        ordering = ['-end_date']


class Skill(models.Model):
    LEVEL = (
        (1, 'I know what it is'),
        (2, 'I am a beginner at it'),
        (3, 'Good at it'),
        (4, 'I did advanced stuff with it'),
        (5, 'I am Pro in it'),
        # TODO Good Scaling system for DL
    )

    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=100)
    level = models.SmallIntegerField(choices=LEVEL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user-cv-index')


class Language(models.Model):
    LANGUAGE = (
        ('english', 'English'),
        ('german', 'German'),
        ('french', 'French'),
        ('portuguese', 'Portuguese'),
        # TODO add possible languages, maybe create a table for this?
    )

    LEVEL = (
        ('understand', 'Understand it'),
        ('speak', 'Understand and speak it'),
        ('fluent', 'fluent'),
        ('mother_tongue', 'mother tongue'),
    )

    user = models.ForeignKey(User, blank=True, null=True)
    language = models.CharField(max_length=100, choices=LANGUAGE)
    level = models.CharField(max_length=100, choices=LEVEL)

    def __str__(self):
        return self.language

    def get_absolute_url(self):
        return reverse('user-cv-index')

