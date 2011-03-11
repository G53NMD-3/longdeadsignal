from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, ListView
from syncr.flickr.models import Photo

urlpatterns = patterns('longdeadsignal.apps.core.views',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),
    
    url(r'^photos/$', ListView.as_view(model=Photo), name='photo_list'),
    url(r'^$', TemplateView.as_view(template_name='core/index.html'), name='index'),
)
