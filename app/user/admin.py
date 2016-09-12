from django.contrib import admin
from .models import Profile, Education, Experience, Language, Skill

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Language)
admin.site.register(Experience)
admin.site.register(Skill)
