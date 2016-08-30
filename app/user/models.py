from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

