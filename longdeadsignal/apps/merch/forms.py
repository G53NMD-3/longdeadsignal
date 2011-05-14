from longdeadsignal.apps.merch.models import Merch
from django.db import IntegrityError
from django.template.defaultfilters import slugify
from django import forms

class MerchForm(forms.ModelForm):
    class Meta:
        model = Merch
    
    def clean_title(self):
        data = self.cleaned_data['title']
        try:
            Merch.objects.get(slug=slugify(data))
        except Merch.DoesNotExist:
            return data
        else:
            raise forms.ValidationError('An item with a similar name already exists')