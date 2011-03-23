# merchs/views.py
import uuid
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from longdeadsignal.apps.merch.models import Merch

def merch_detail(request, slug):
    merch = get_object_or_404(Merch, slug=slug)
    paypal = {
        'amount': merch.price,
        'item_name': merch.title,
        'item_number': merch.slug,
        'currency_code': 'GBP',
        
        # PayPal wants a unique invoice ID
        'invoice': str(uuid.uuid1()), 
        
        # It'll be a good idea to setup a SITE_DOMAIN inside settings
        # so you don't need to hardcode these values.
        'return_url': settings.SITE_DOMAIN + 'merch/thanks',
        'cancel_return': settings.SITE_DOMAIN + 'merch/' + merch.slug,
    }
    form = PayPalPaymentsForm(initial=paypal)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()
    return render_to_response('merch/merch_detail.html', {
        'merch' : merch,
        'form' : rendered_form,
    }, RequestContext(request))
