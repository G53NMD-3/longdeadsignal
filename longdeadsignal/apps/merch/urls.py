from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from longdeadsignal.apps.merch.models import Merch

urlpatterns = patterns('',
    url(r'^(?P<slug>[^/]+)/$', 'apps.merch.views.merch_detail'),
    url(r'^$', ListView.as_view(model=Merch), name='merch_list'),
)
