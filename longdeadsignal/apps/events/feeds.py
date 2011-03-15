from django.contrib.syndication.views import Feed
from longdeadsignal.apps.events.models import Event
from longdeadsignal.apps.events import settings as app_settings
import datetime

class EventFeed(Feed):
    title = 'Events Feed'
    link = '/events/'
    
    def items(self):
        return Event.objects.order_by('-pub_date')[:app_settings.EVENT_FEED_ITEM_COUNT]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.pre_event_message_html
    
    def item_pubdate(self, item):
        return item.date