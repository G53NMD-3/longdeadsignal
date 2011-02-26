from django.conf import settings

PAGINATE_BY = getattr(settings, 'NEWS_PAGINATE_BY', 10)