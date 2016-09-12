from django.contrib import admin
from .models import Company, Sector, Job, ApplicationElement, ApplicationProcess

# Register your models here.
admin.site.register(Company)
admin.site.register(Sector)
admin.site.register(Job)
admin.site.register(ApplicationElement)
admin.site.register(ApplicationProcess)
