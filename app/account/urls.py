from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

urlpatterns = [

    url(r'^login/$', auth_views.login,
        {
            'template_name': 'account/login.html'
        },
        name='login'),

    url(r'^logout/$', auth_views.logout,
        {
            'next_page': '/'
        },
        name='logout'),

    url(r'^password_change/$', auth_views.password_change,
        {
            'template_name': 'account/password_change.html'
        },
        name='password_change'),

    url(r'^password_change/done/$', auth_views.password_change_done,
        {
            'template_name': 'account/password_change_done.html'
        },
        name='password_change_done'),

    url(r'^password_reset/$', auth_views.password_reset,
        {
            'template_name': 'account/password_reset.html',
            'email_template_name': 'account/password_reset_email.html',
            'subject_template_name': 'account/password_reset_subject.txt',
        }, name='password_reset'),

    url(r'^password_reset/done/$', auth_views.password_reset_done,
        {
            'template_name': 'account/password_reset_done.html'
        },
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {
            'template_name': 'account/password_reset_confirm.html'
        },
        name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.password_reset_complete,
        {
            'template_name': 'account/password_reset_complete.html'
        },
        name='password_reset_complete'),

]
