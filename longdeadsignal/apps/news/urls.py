from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from longdeadsignal.apps.news.models import Post

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),
    
    url(r'^(?P<slug>[^/]+)/', DetailView.as_view(
        model=Post,
        context_object_name='post',
    ), name='post_detail'),
    
    url(r'^$', ListView.as_view(
        model=Post,
        context_object_name='posts',
    ), name='post_list'),
)
