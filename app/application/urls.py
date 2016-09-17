from django.conf.urls import url

from .views import ProcessView, ProcessCreateView, ProcessUpdateView, ProcessDeleteView, CompanyApplicationListView, \
    CompanyQueueListView, UserApplicationListView, UserQueueListView

urlpatterns = [

    url(r'^(?P<company_slug>[\w-]+)/process/$', ProcessView.as_view(),
        name='application-process-list'),
    url(r'^(?P<company_slug>[\w-]+)/process/create/$', ProcessCreateView.as_view(),
        name='application-process-create'),
    url(r'^(?P<company_slug>[\w-]+)/process/update/(?P<pk>[0-9]+)/$', ProcessUpdateView.as_view(),
        name='application-process-update'),
    url(r'^(?P<company_slug>[\w-]+)/process/delete/(?P<pk>[0-9]+)/$', ProcessDeleteView.as_view(),
        name='application-process-delete'),


    url(r'^company/(?P<company_slug>[\w-]+)/$', CompanyApplicationListView.as_view(),
        name='application-company-application-list'),
    url(r'^company/(?P<company_slug>[\w-]+)/(?P<pk>[0-9]+)/$', CompanyQueueListView.as_view(),
        name='application-company-queue-list'),
    url(r'^user/(?P<username>[\w-]+)/$', UserApplicationListView.as_view(),
        name='application-user-application-list'),
    url(r'^user/0(?P<username>[\w-]+)/(?P<pk>[0-9]+)/$', UserQueueListView.as_view(),
        name='application-user-queue-list'),

]
