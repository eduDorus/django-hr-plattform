from django.conf.urls import url
from django.views.generic import TemplateView

from .views import UserFormView, ProfileView, ProfileEdit, JobListView, apply_for_job, JobDetailView, CVView, \
    EducationCreate, EducationUpdate, EducationDelete, ExperienceCreate, ExperienceUpdate, ExperienceDelete, SkillList, \
    SkillCreate, SkillUpdate, SkillDelete, LanguageList, LanguageCreate, LanguageUpdate, LanguageDelete

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='user/home.html'), name='user-home'),

    url(r'^registration/$', UserFormView.as_view(), name='registration'),

    url(r'^(?P<pk>[0-9]+)/profile/$', ProfileView.as_view(), name='user-profile'),
    url(r'^(?P<pk>[0-9]+)/profile/edit/$', ProfileEdit.as_view(), name='user-profile-edit'),

    url(r'^job-search/$', JobListView.as_view(), name='user-job-list'),
    url(r'^job/(?P<pk>[0-9]+)/detail/$', JobDetailView.as_view(), name='user-job-detail'),
    url(r'^job/(?P<pk>[0-9]+)/job-application/$', apply_for_job, name='user-job-application'),

    url(r'^cv/$', CVView.as_view(), name='cv-index'),

    url(r'^cv/(?P<user_id>[0-9]+)/education/add/$', EducationCreate.as_view(), name='education-add'),
    url(r'^cv/(?P<user_id>[0-9]+)/education/(?P<pk>[0-9]+)/edit/$', EducationUpdate.as_view(), name='education-update'),
    url(r'^cv/(?P<user_id>[0-9]+)/education/(?P<pk>[0-9]+)/delete/$', EducationDelete.as_view(),
        name='education-delete'),

    url(r'^CV/(?P<user_id>[0-9]+)/experience/add/$', ExperienceCreate.as_view(), name='experience-add'),
    url(r'^CV/(?P<user_id>[0-9]+)/experience/(?P<pk>[0-9]+)/edit/$', ExperienceUpdate.as_view(),
        name='experience-update'),
    url(r'^CV/(?P<user_id>[0-9]+)/experience/(?P<pk>[0-9]+)/delete/$', ExperienceDelete.as_view(),
        name='experience-delete'),

    url(r'^CV/(?P<user_id>[0-9]+)/skill/$', SkillList.as_view(), name='skill-list'),
    url(r'^CV/(?P<user_id>[0-9]+)/skill/add/$', SkillCreate.as_view(), name='skill-add'),
    url(r'^CV/(?P<user_id>[0-9]+)/skill/(?P<pk>[0-9]+)/edit/$', SkillUpdate.as_view(), name='skill-update'),
    url(r'^CV/(?P<user_id>[0-9]+)/skill/(?P<pk>[0-9]+)/delete/$', SkillDelete.as_view(), name='skill-delete'),

    url(r'^CV/(?P<user_id>[0-9]+)/language/$', LanguageList.as_view(), name='language-list'),
    url(r'^CV/(?P<user_id>[0-9]+)/language/add/$', LanguageCreate.as_view(), name='language-add'),
    url(r'^CV/(?P<user_id>[0-9]+)/language/(?P<pk>[0-9]+)/edit/$', LanguageUpdate.as_view(),
        name='language-update'),
    url(r'^CV/(?P<user_id>[0-9]+)/language/(?P<pk>[0-9]+)/delete/$', LanguageDelete.as_view(),
        name='language-delete'),

]
