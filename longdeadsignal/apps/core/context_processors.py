from django.contrib.sites.models import Site
from django.conf import settings

def site_name(request):
    try:
        site = Site.objects.get_current()
    except:
        return {}
    else:
        return {
            'SITE_NAME': site.name,
            'SITE_DOMAIN': site.domain,
        }

def usernames(request):
    return {
        'FLICKR_USERNAME': settings.FLICKR_USERNAME,
    }