from django.conf import settings

GLOBAL_FEED_ITEM_COUNT = getattr(settings, 'GLOBAL_FEED_ITEM_COUNT', 10)