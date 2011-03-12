from django.contrib import admin
from longdeadsignal.apps.music.models import Song, Album

admin.site.register(Song)
admin.site.register(Album)