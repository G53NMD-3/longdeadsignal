from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, ListView, UpdateView, \
    CreateView
from longdeadsignal.apps.news.models import Post
from longdeadsignal.apps.badmin.views import PostBadminUpdateView, \
    PostBadminCreateView
import settings as app_settings
from django.contrib.auth.decorators import login_required

news_patterns = patterns('', 
    url(r'^$', login_required(ListView.as_view(
        model=Post,
        template_name='badmin/news/post_list.html',
        paginate_by=app_settings.PAGINATE_BY,
    )), name='post_list'),
    
    url(r'^new-post/$', login_required(PostBadminCreateView.as_view()), name='post_create'),
    
    url(r'^page/(?P<page>[0-9]+)/$', login_required(ListView.as_view(
        model=Post,
        template_name='badmin/news/post_list.html',
        paginate_by=app_settings.PAGINATE_BY,
    )), name='post_list'),
    
    url(r'^(?P<slug>[^/]+)/$', login_required(PostBadminUpdateView.as_view()), name='post_update')
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),
    
    url(r'^news/', include(news_patterns, namespace='news'), name='news'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    
    url(r'^$', login_required(TemplateView.as_view(
        template_name='badmin/index.html',
    )), name='index'),
)