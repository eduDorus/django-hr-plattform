from django.contrib import admin
from .models import Company, Sector, Job, Skill, Task, Preference

# Register your models here.
admin.site.register(Company)
admin.site.register(Sector)

admin.site.register(Job)
admin.site.register(Task)
admin.site.register(Skill)
admin.site.register(Preference)
