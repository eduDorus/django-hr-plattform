from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CompanyUserFormView, CompanyProfileView, CompanyProfileEdit

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='company/home.html'), name='company-home'),

    url(r'^registration/$', CompanyUserFormView.as_view(), name='company-registration'),

    url(r'^profile/(?P<pk>[0-9]+)/$', CompanyProfileView.as_view(), name='company-profile'),
    url(r'^profile/(?P<pk>[0-9]+)/edit$', CompanyProfileEdit.as_view(), name='company-profile-edit'),

]
