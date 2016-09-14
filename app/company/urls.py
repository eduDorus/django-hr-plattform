from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CompanyUserFormView, CompanyProfileDetailView, CompanyProfileUpdateView, JobListView, JobUpdateView, \
    JobCreateView, JobDeleteView, ApplicationProcessView, ApplicationProcessCreateView, ApplicationProcessUpdateView, \
    ApplicationProcessDeleteView, JobDetailView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='company/home.html'), name='company-home'),

    url(r'^registration/$', CompanyUserFormView.as_view(), name='company-registration'),

    url(r'^(?P<pk>[0-9]+)/jobs/$', JobListView.as_view(), name='company-job-list'),
    url(r'^(?P<pk>[0-9]+)/jobs/create/$', JobCreateView.as_view(), name='company-job-create'),
    url(r'^(?P<pk>[0-9]+)/jobs/detail/$', JobDetailView.as_view(), name='company-job-detail'),
    url(r'^(?P<pk>[0-9]+)/jobs/update/$', JobUpdateView.as_view(), name='company-job-update'),
    url(r'^(?P<pk>[0-9]+)/jobs/delete/$', JobDeleteView.as_view(), name='company-job-delete'),

    url(r'^(?P<pk>[0-9]+)/profile/$', CompanyProfileDetailView.as_view(), name='company-profile'),
    url(r'^(?P<pk>[0-9]+)/profile/update/$', CompanyProfileUpdateView.as_view(), name='company-profile-update'),

    url(r'^(?P<pk>[0-9]+)/application-process/$', ApplicationProcessView.as_view(),
        name='company-application-process-list'),
    url(r'^(?P<pk>[0-9]+)/application-process/create/$', ApplicationProcessCreateView.as_view(),
        name='company-application-process-create'),
    url(r'^(?P<pk>[0-9]+)/application-process/update/(?P<pk_a>[0-9]+)/$', ApplicationProcessUpdateView.as_view(),
        name='company-application-process-update'),
    url(r'^(?P<pk>[0-9]+)/application-process/delete/(?P<pk_a>[0-9]+)/$', ApplicationProcessDeleteView.as_view(),
        name='company-application-process-delete'),

]
