from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('longdeadsignal.apps.core.views',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),
    
    url(r'^$', 'index'),
)
