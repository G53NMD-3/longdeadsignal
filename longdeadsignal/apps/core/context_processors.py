from django.contrib.sites.models import Site

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