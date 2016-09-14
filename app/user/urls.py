from django.conf.urls import url
from django.views.generic import TemplateView

from .views import UserFormView, ProfileView, ProfileEdit, JobListView, apply_for_job, JobDetailView, CVView, \
    EducationCreate, EducationUpdate, EducationDelete, ExperienceCreate, ExperienceUpdate, ExperienceDelete, SkillList, \
    SkillCreate, SkillUpdate, SkillDelete, LanguageList, LanguageCreate, LanguageUpdate, LanguageDelete

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='user/home.html'), name='user-home'),

    url(r'^registration/$', UserFormView.as_view(), name='registration'),

    url(r'^(?P<username>[\w-]+)/profile/$', ProfileView.as_view(), name='user-profile'),
    url(r'^(?P<username>[\w-]+)/profile/edit/$', ProfileEdit.as_view(), name='user-profile-edit'),

    url(r'^job-search/$', JobListView.as_view(), name='user-job-list'),
    url(r'^job/(?P<pk>[0-9]+)/detail/$', JobDetailView.as_view(), name='user-job-detail'),
    url(r'^job/(?P<pk>[0-9]+)/job-application/$', apply_for_job, name='user-job-application'),

    url(r'^(?P<username>[\w-]+)/cv/$', CVView.as_view(), name='user-cv-index'),

    url(r'^(?P<username>[\w-]+)/cv/education/add/$', EducationCreate.as_view(), name='user-education-add'),
    url(r'^(?P<username>[\w-]+)/cv/education/(?P<pk>[0-9]+)/edit/$', EducationUpdate.as_view(), name='user-education-update'),
    url(r'^(?P<username>[\w-]+)/cv/education/(?P<pk>[0-9]+)/delete/$', EducationDelete.as_view(),
        name='user-education-delete'),

    url(r'^(?P<username>[\w-]+)/cv/experience/add/$', ExperienceCreate.as_view(), name='user-experience-add'),
    url(r'^(?P<username>[\w-]+)/cv/experience/(?P<pk>[0-9]+)/edit/$', ExperienceUpdate.as_view(),
        name='user-experience-update'),
    url(r'^(?P<username>[\w-]+)/cv/experience/(?P<pk>[0-9]+)/delete/$', ExperienceDelete.as_view(),
        name='user-experience-delete'),

    url(r'^(?P<username>[\w-]+)/cv/skill/$', SkillList.as_view(), name='user-skill-list'),
    url(r'^(?P<username>[\w-]+)/cv/skill/add/$', SkillCreate.as_view(), name='user-skill-add'),
    url(r'^(?P<username>[\w-]+)/cv/skill/(?P<pk>[0-9]+)/edit/$', SkillUpdate.as_view(), name='user-skill-update'),
    url(r'^(?P<username>[\w-]+)/cv/skill/(?P<pk>[0-9]+)/delete/$', SkillDelete.as_view(), name='user-skill-delete'),

    url(r'^(?P<username>[\w-]+)/cv/language/$', LanguageList.as_view(), name='user-language-list'),
    url(r'^(?P<username>[\w-]+)/cv/language/add/$', LanguageCreate.as_view(), name='user-language-add'),
    url(r'^(?P<username>[\w-]+)/cv/language/(?P<pk>[0-9]+)/edit/$', LanguageUpdate.as_view(),
        name='user-language-update'),
    url(r'^(?P<username>[\w-]+)/cv/language/(?P<pk>[0-9]+)/delete/$', LanguageDelete.as_view(),
        name='user-language-delete'),

]
