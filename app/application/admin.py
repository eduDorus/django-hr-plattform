from django.contrib import admin
from .models import Process, Queue, Application

admin.register.site(Process)
admin.register.site(Queue)
admin.register.site(Application)
