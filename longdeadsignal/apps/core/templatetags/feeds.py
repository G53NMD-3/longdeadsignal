from django import template
from django.conf import settings
from syncr.flickr.models import Photo

register = template.Library()

@register.simple_tag
def youtube_feed():
    return 'http://gdata.youtube.com/feeds/base/users/%s/uploads?alt=rss&v=2&orderby=published' % settings.YOUTUBE_USERNAME

@register.simple_tag
def flickr_feed():
    photo = Photo.objects.latest()
    return 'http://api.flickr.com/services/feeds/photos_public.gne?id=%s&lang=en-us' % photo.owner_nsid