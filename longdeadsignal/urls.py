from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'longdeadsignal.views.home', name='home'),
    # url(r'^longdeadsignal/', include('longdeadsignal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^django-admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^django-admin/', include(admin.site.urls)),
    
    # The bespoke longdeadsignal apps
    url(r'^music/', include('longdeadsignal.apps.music.urls', namespace='music')),
    url(r'^events/', include('longdeadsignal.apps.events.urls', namespace='events')),
    url(r'^news/', include('longdeadsignal.apps.news.urls', namespace='news')),
    url(r'^admin/', include('longdeadsignal.apps.badmin.urls', namespace='badmin')),
    
    # Catch any unmatched URLs and send them to the core app
    url(r'', include('longdeadsignal.apps.core.urls', namespace='core')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )