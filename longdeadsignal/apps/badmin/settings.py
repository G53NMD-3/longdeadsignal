from django.conf import settings

PAGINATE_BY = getattr(settings, 'BADMIN_PAGINATE_BY', 10)