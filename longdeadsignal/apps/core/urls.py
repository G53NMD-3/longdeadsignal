from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),
    
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'core/index.html',
    }),
)
