from django.conf import settings

PAGINATE_BY = getattr(settings, 'NEWS_PAGINATE_BY', 10)
POST_FEED_ITEM_COUNT = getattr(settings, 'NEW_POST_FEED_ITEM_COUNT', 10)