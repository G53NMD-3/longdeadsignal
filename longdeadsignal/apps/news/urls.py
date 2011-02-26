from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from longdeadsignal.apps.news.models import Post
import settings as app_settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),
    
    url(r'^(?P<year>(19|20)\d\d)/$', YearArchiveView.as_view(
        model=Post,
        date_field='pub_date',
        make_object_list=True
    ), name='post_archive_year'),
    
    url(r'^(?P<year>(19|20)\d\d)/(?P<month>[A-Z|a-z][a-z]{2})/$', MonthArchiveView.as_view(
        model=Post,
        date_field='pub_date',
    ), name='post_archive_month'),
    
    url(r'^page/(?P<page>[0-9]+)/$', ListView.as_view(model=Post, paginate_by=app_settings.PAGINATE_BY), name='post_list'),
    url(r'^(?P<slug>[^/]+)/$', DetailView.as_view(model=Post), name='post_detail'),
    url(r'^$', ListView.as_view(model=Post, paginate_by=app_settings.PAGINATE_BY), name='post_list'),
)