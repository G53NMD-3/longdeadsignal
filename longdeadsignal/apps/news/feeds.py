from django.contrib.syndication.views import Feed
from longdeadsignal.apps.news.models import Post

from longdeadsignal.apps.news import settings as app_settings

class PostFeed(Feed):
    title = 'New Feed'
    link = '/news/'
    
    def items(self):
        return Post.objects.order_by('-pub_date')[:app_settings.POST_FEED_ITEM_COUNT]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.body_html
    
    def item_pubdate(self, item):
        return item.pub_date