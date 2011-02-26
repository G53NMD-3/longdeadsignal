from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # The bespoke longdeadsignal apps
    url(r'^news/', include('longdeadsignal.apps.news.urls', namespace='news')),
    
    # Catch any unmatched URLs and send them to the core app
    url(r'', include('longdeadsignal.apps.core.urls', namespace='core')),
)
