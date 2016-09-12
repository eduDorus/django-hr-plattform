from django.conf.urls import url
from django.views.generic import TemplateView

from .views import UserFormView, ProfileView, ProfileEdit, JobListView, apply_for_job, JobDetailView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='user/home.html'), name='user-home'),

    url(r'^registration/$', UserFormView.as_view(), name='registration'),

    url(r'^(?P<pk>[0-9]+)/profile/$', ProfileView.as_view(), name='user-profile'),
    url(r'^(?P<pk>[0-9]+)/profile/edit/$', ProfileEdit.as_view(), name='user-profile-edit'),

    url(r'^job-search/$', JobListView.as_view(), name='user-job-list'),
    url(r'^job/(?P<pk>[0-9]+)/detail/$', JobDetailView.as_view(), name='user-job-detail'),
    url(r'^job/(?P<pk>[0-9]+)/job-application/$', apply_for_job, name='user-job-application'),

]


