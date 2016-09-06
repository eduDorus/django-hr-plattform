from django.conf.urls import url
from django.views.generic import TemplateView

from .views import UserFormView, ProfileView, ProfileEdit

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='user/home.html'), name='user-home'),

    url(r'^registration/$', UserFormView.as_view(), name='registration'),

    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileView.as_view(), name='user-profile'),
    url(r'^profile/(?P<pk>[0-9]+)/edit$', ProfileEdit.as_view(), name='user-profile-edit'),

]
