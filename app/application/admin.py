from django.contrib import admin
from .models import Process, Queue, Application

admin.site.register(Process)
admin.site.register(Queue)
admin.site.register(Application)
