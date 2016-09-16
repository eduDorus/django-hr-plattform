from django.contrib.auth.models import User
from django.db import models


class Process(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('company.Company')

    def __str__(self):
        return "%s: %s" % (self.company.name, self.name)


class Queue(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()
    # TODO status field?
    description = models.CharField(max_length=1000)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.process.company.name, self.name)


class Application(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey('company.Job')
    queue = models.ForeignKey(Queue)

    def __str__(self):
        return "%s: %s in %s" % (self.user, self.job.title, self.queue.name)
