from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from longdeadsignal.apps.music.models import Album, Song

urlpatterns = patterns('',
    url(r'^(?P<slug>[^/]+)/$', DetailView.as_view(model=Album), name='album_Detail'),
    url(r'^$', ListView.as_view(model=Album), name='album_list'),
)