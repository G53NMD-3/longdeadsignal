from django.contrib.syndication.views import Feed
from longdeadsignal.apps.news.models import Post
from longdeadsignal.apps.events.models import Event
from syncr.youtube.models import Video
from syncr.flickr.models import Photo
from longdeadsignal.apps.core import settings as app_settings
import datetime
import operator

class GlobalFeed(Feed):
    title = 'All Updates'
    link = '/'
    
    def items(self):
        video_list = Video.objects.order_by('-published')[:app_settings.GLOBAL_FEED_ITEM_COUNT]
        photo_list = Photo.objects.order_by('-upload_date')[:app_settings.GLOBAL_FEED_ITEM_COUNT]
        post_list = Post.objects.order_by('-pub_date')[:app_settings.GLOBAL_FEED_ITEM_COUNT]
        event_list = Event.objects.order_by('-pub_date')[:app_settings.GLOBAL_FEED_ITEM_COUNT]
        
        # Put them all into a single list
        items = []
        items.extend({
            'title': video.title,
            'description': video.description,
            'pub_date': video.published,
            'url': video.url,
        } for video in video_list)
        items.extend({
            'title': photo.title,
            'description': photo.description,
            'pub_date': photo.upload_date,
            'url': photo.photopage_url,
        } for photo in photo_list)
        items.extend({
            'title': post.title,
            'description': post.body_html,
            'pub_date': post.pub_date,
            'url': post.get_absolute_url(),
        } for post in post_list)
        items.extend({
            'title': event.title,
            'description': event.pre_event_message_html,
            'pub_date': event.date,
            'url': event.get_absolute_url(),
        } for event in event_list)
        
        # Sort the list based upon the time each was added
        return sorted(items, key=operator.itemgetter('pub_date'), reverse=True)
    
    def item_title(self, item):
        return item['title']
    
    def item_description(self, item):
        return item['description']
    
    def item_pubdate(self, item):
        return item['pub_date']
    
    def item_link(self, item):
        return item['url']