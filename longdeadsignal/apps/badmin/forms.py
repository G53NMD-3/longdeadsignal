from django.views.generic.simple import direct_to_template
from django.contrib.formtools.wizard import FormWizard
from django.contrib import admin
from django import forms
from wmd import widgets as wmd_widgets
from longdeadsignal.apps.events.models import Event
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.template.defaultfilters import slugify
import datetime

class CreateEventForm1(forms.Form):
    title = forms.CharField(max_length=100)
    
    location_title = forms.CharField(max_length=100, required=False)
    
    location_address_1 = forms.CharField(max_length=100, required=False)
    location_address_2 = forms.CharField(max_length=100, required=False)
    location_address_3 = forms.CharField(max_length=100, required=False)
    
    location_city = forms.CharField(max_length=100, required=False)
    location_post_code = forms.CharField(max_length=100, required=False)
    location_country = forms.CharField(max_length=100, required=False)
    
    date = forms.DateTimeField()
    
    def clean_title(self):
        data = self.cleaned_data['title']
        try:
            Event.objects.get(slug=slugify(data))
        except Event.DoesNotExist:
            return data
        else:
            raise forms.ValidationError('An event with a similar name already exists')

class CreateEventForm2(forms.Form):
    pre_event_message_markdown = forms.CharField(widget=wmd_widgets.MarkDownInput())

class CreateEventForm3(forms.Form):
    location_google_maps = forms.CharField(max_length=100)


class CreateEventWizard(FormWizard):
    def done(self, request, form_list):
        data = form_list[0].cleaned_data
        data.update(form_list[1].cleaned_data)
        data.update(form_list[2].cleaned_data)
        try:
            event = Event.objects.create(**data)
        except IntegrityError:
            return direct_to_template(request, 'badmin/events/event_failed.html', {
                'data': data,
            })
        else:
            return HttpResponseRedirect(event.get_absolute_url())
    
    def get_template(self, step):
        return 'badmin/events/event_create_wizard_%d.html' % (int(step) + 1)