from django.conf.urls import url
from .views import ProcessView, ProcessCreateView, ProcessUpdateView, ProcessDeleteView

urlpatterns = [

    url(r'^(?P<company_slug>[\w-]+)/application/process/$', ProcessView.as_view(),
        name='application-process-list'),
    url(r'^(?P<company_slug>[\w-]+)/application/process/create/$', ProcessCreateView.as_view(),
        name='application-process-create'),
    url(r'^(?P<company_slug>[\w-]+)/application/process/update/(?P<pk>[0-9]+)/$', ProcessUpdateView.as_view(),
        name='application-process-update'),
    url(r'^(?P<company_slug>[\w-]+)/application/process/delete/(?P<pk>[0-9]+)/$', ProcessDeleteView.as_view(),
        name='application-process-delete'),

]