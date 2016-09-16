from django.conf.urls import url
from django.views.generic import TemplateView

from .views import UserFormView, ProfileDetailView, ProfileUpdateView, JobListView, apply_for_job, JobDetailView, CVView, \
    EducationCreateView, EducationUpdateView, EducationDeleteView, ExperienceCreateView, ExperienceUpdateView, ExperienceDeleteView, SkillListView, \
    SkillCreateView, SkillUpdateView, SkillDeleteView, LanguageListView, LanguageCreateView, LanguageUpdateView, LanguageDeleteView

urlpatterns = [
    # User Teaser View
    url(r'^$', TemplateView.as_view(template_name='user/home.html'), name='user-home'),

    # Company Teaser View
    url(r'^dashboard/$', TemplateView.as_view(template_name='user/dashboard.html'), name='user-dashboard'),

    # User Registration
    url(r'^registration/$', UserFormView.as_view(), name='user-registration'),

    # User Profile
    url(r'^(?P<username>[\w-]+)/profile/$', ProfileDetailView.as_view(), name='user-profile'),
    url(r'^(?P<username>[\w-]+)/profile/edit/$', ProfileUpdateView.as_view(), name='user-profile-edit'),

    url(r'^job-search/$', JobListView.as_view(), name='user-job-list'),
    url(r'^job/(?P<pk>[0-9]+)/detail/$', JobDetailView.as_view(), name='user-job-detail'),
    url(r'^job/(?P<pk>[0-9]+)/job-application/$', apply_for_job, name='user-job-application'),

    # CV View
    url(r'^(?P<username>[\w-]+)/cv/$', CVView.as_view(), name='user-cv-index'),

    # CV Education
    url(r'^(?P<username>[\w-]+)/cv/education/add/$', EducationCreateView.as_view(), name='user-education-add'),
    url(r'^(?P<username>[\w-]+)/cv/education/(?P<pk>[0-9]+)/edit/$', EducationUpdateView.as_view(),
        name='user-education-update'),
    url(r'^(?P<username>[\w-]+)/cv/education/(?P<pk>[0-9]+)/delete/$', EducationDeleteView.as_view(),
        name='user-education-delete'),

    # CV Experience
    url(r'^(?P<username>[\w-]+)/cv/experience/add/$', ExperienceCreateView.as_view(), name='user-experience-add'),
    url(r'^(?P<username>[\w-]+)/cv/experience/(?P<pk>[0-9]+)/edit/$', ExperienceUpdateView.as_view(),
        name='user-experience-update'),
    url(r'^(?P<username>[\w-]+)/cv/experience/(?P<pk>[0-9]+)/delete/$', ExperienceDeleteView.as_view(),
        name='user-experience-delete'),

    # CV Skills
    url(r'^(?P<username>[\w-]+)/cv/skill/$', SkillListView.as_view(), name='user-skill-list'),
    url(r'^(?P<username>[\w-]+)/cv/skill/add/$', SkillCreateView.as_view(), name='user-skill-add'),
    url(r'^(?P<username>[\w-]+)/cv/skill/(?P<pk>[0-9]+)/edit/$', SkillUpdateView.as_view(), name='user-skill-update'),
    url(r'^(?P<username>[\w-]+)/cv/skill/(?P<pk>[0-9]+)/delete/$', SkillDeleteView.as_view(), name='user-skill-delete'),

    # CV Language
    url(r'^(?P<username>[\w-]+)/cv/language/$', LanguageListView.as_view(), name='user-language-list'),
    url(r'^(?P<username>[\w-]+)/cv/language/add/$', LanguageCreateView.as_view(), name='user-language-add'),
    url(r'^(?P<username>[\w-]+)/cv/language/(?P<pk>[0-9]+)/edit/$', LanguageUpdateView.as_view(),
        name='user-language-update'),
    url(r'^(?P<username>[\w-]+)/cv/language/(?P<pk>[0-9]+)/delete/$', LanguageDeleteView.as_view(),
        name='user-language-delete'),
]
