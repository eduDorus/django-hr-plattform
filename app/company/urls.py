from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CompanyUserFormView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='company/home.html'), name='company-home'),

    url(r'^registration/$', CompanyUserFormView.as_view(), name='company-registration'),

]
