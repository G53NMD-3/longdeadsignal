from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, ListView, DetailView
from syncr.flickr.models import Photo
from syncr.youtube.models import Video
from longdeadsignal.apps.core.views import IndexTemplateView

urlpatterns = patterns('longdeadsignal.apps.core.views',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),
    
    url(r'^photos/$', ListView.as_view(model=Photo), name='photo_list'),
    url(r'^videos/$', ListView.as_view(model=Video), name='video_list'),
    url(r'^videos/(?P<slug>[^/]+)/$', DetailView.as_view(model=Video, slug_field='video_id'), name='video_detail'),
    url(r'^$', IndexTemplateView.as_view(), name='index'),
)
