from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, ListView, UpdateView
from longdeadsignal.apps.news.models import Post
from longdeadsignal.apps.news.forms import PostForm
from longdeadsignal.apps.badmin.views import PostBadminUpdateView
import settings as app_settings

news_patterns = patterns('', 
    url(r'^$', ListView.as_view(
        model=Post,
        template_name='badmin/news/post_list.html',
        paginate_by=app_settings.PAGINATE_BY,
    ), name='post_list'),
    
    url(r'^page/(?P<page>[0-9]+)/$', ListView.as_view(
        model=Post,
        template_name='badmin/news/post_list.html',
        paginate_by=app_settings.PAGINATE_BY,
    ), name='post_list'),
    
    url(r'^(?P<slug>[^/]+)/$', PostBadminUpdateView.as_view(), name='post_update')
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),
    
    url(r'^news/', include(news_patterns, namespace='news'), name='news'),
    
    url(r'^$', TemplateView.as_view(
        template_name='badmin/index.html',
    ), name='index'),
)