from django.conf.urls import url
from django.views.generic import TemplateView

from .views import UserFormView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='user/home.html'), name='user-home'),

    url(r'^registration/$', UserFormView.as_view(), name='registration'),

]
