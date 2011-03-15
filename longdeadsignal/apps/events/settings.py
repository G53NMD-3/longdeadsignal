from django.conf import settings

EVENT_FEED_ITEM_COUNT = getattr(settings, 'EVENTS_EVENT_FEED_ITEM_COUNT', 10)