from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from longdeadsignal.apps.events.models import Event
from longdeadsignal.apps.events.feeds import EventFeed

urlpatterns = patterns('',
    url(r'^(?P<year>(19|20)\d\d)/$', YearArchiveView.as_view(
        model=Event,
        date_field='date',
        make_object_list=True
    ), name='event_archive_year'),
    
    url(r'^(?P<year>(19|20)\d\d)/(?P<month>[A-Z|a-z][a-z]{2})/$', MonthArchiveView.as_view(
        model=Event,
        date_field='date',
    ), name='event_archive_month'),
    
    url(r'^feed/$', EventFeed(), name='feed'),
    
    url(r'^(?P<slug>[^/]+)/$', DetailView.as_view(model=Event), name='event_detail'),
    url(r'^page/(?P<page>[0-9]+)/$', ListView.as_view(model=Event), name='event_list'),
    url(r'^$', ListView.as_view(model=Event), name='event_list'),
)