from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CompanyUserFormView, CompanyProfileDetailView, CompanyProfileUpdateView, JobListView, JobUpdateView, \
    JobCreateView, JobDeleteView, JobDetailView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='company/home.html'), name='company-home'),

    url(r'^registration/$', CompanyUserFormView.as_view(), name='company-registration'),

    url(r'^(?P<company_slug>[\w-]+)/job-list/$', JobListView.as_view(), name='company-job-list'),
    url(r'^(?P<company_slug>[\w-]+)/job/create/$', JobCreateView.as_view(), name='company-job-create'),
    url(r'^(?P<company_slug>[\w-]+)/job/(?P<pk>[0-9]+)/detail/$', JobDetailView.as_view(), name='company-job-detail'),
    url(r'^(?P<company_slug>[\w-]+)/job/(?P<pk>[0-9]+)/update/$', JobUpdateView.as_view(), name='company-job-update'),
    url(r'^(?P<company_slug>[\w-]+)/job/(?P<pk>[0-9]+)/delete/$', JobDeleteView.as_view(), name='company-job-delete'),

    url(r'^(?P<company_slug>[\w-]+)/profile/$', CompanyProfileDetailView.as_view(), name='company-profile'),
    url(r'^(?P<company_slug>[\w-]+)/profile/update/$', CompanyProfileUpdateView.as_view(), name='company-profile-update'),

]
