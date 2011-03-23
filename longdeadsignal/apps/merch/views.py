from django.views.generic import DetailView
from longdeadsignal.apps.merch.models import Merch
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

class MerchDetailView(DetailView):
    model = Merch
    context_object_name = 'merch'
    
    def get_context_data(self, **kwargs):
        context = super(MerchDetailView, self).get_context_data(**kwargs)
        merch = context['merch']
        paypal = {
            'amount': merch.price,
            'item_name': merch.title,
            'item_number': merch.slug,
            'currency_code': 'GBP',
            
            # PayPal wants a unique invoice ID
            'invoice': str(uuid.uuid4()),
            
            'return_url': '/merch/thanks',
            'cancel_return': merch.get_absolute_url(),
        }
        form = PayPalPaymentsForm(initial=paypal)
        context['form'] = form.sandbox() if settings.DEBUG else form.render()
        return context