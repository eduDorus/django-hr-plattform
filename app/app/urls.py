"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^application/', include('application.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^application/', include('application.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
