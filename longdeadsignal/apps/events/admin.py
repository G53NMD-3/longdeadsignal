from django.contrib import admin
from longdeadsignal.apps.events.models import Event, EventMediaItem

admin.site.register(Event)
admin.site.register(EventMediaItem)