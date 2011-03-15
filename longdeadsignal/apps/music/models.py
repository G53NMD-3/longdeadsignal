from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import datetime
import os

class Song(models.Model):
    # The title of the song, its name
    title = models.CharField(max_length=100)
    slug = models.SlugField(db_index=True, editable=False)
    
    def _get_upload_path(instance, filename):
        if instance.slug is None:
            instance.slug = slugify(instance.title)
        return os.path.join(
            settings.ALBUM_UPLOAD_PATH,
            instance.album.slug,
            instance.slug,
            '%s%s' % (instance.slug, os.path.splitext(filename)[1])
        )
    
    # Song files to be played in the browser via HTML5 
    song_mp3 = models.FileField(upload_to=_get_upload_path, blank=True)
    song_ogg = models.FileField(upload_to=_get_upload_path, blank=True)
    
    # Whether website users can actually listen to the song or not
    can_listen = models.BooleanField(default=False)
    
    # The album this song belongs to
    album = models.ForeignKey('music.Album', blank=True)
    
    # The position at which this track fits in the album
    track_number = models.PositiveIntegerField(db_index=True)
    
    # The date and time this song was added to the database
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('album', 'track_number')
    
    def __unicode__(self):
        return u'%s - %02d %s' % (self.album.title, self.track_number, self.title)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Song, self).save(*args, **kwargs)


class Album(models.Model):
    # The title of the album
    title = models.CharField(max_length=100)
    slug = models.SlugField(db_index=True, editable=False)
    
    def _get_upload_path(instance, filename):
        if instance.slug is None:
            instance.slug = slugify(instance.title)
        return os.path.join(
            settings.ALBUM_UPLOAD_PATH,
            instance.slug,
            '%s%s' % (settings.ALBUM_ARTWORK_FILE_NAME, os.path.splitext(filename)[1]),
        )
    
    # The artwork for the front cover of the album
    artwork = models.FileField(upload_to=_get_upload_path, blank=True)
    
    # The date this album was released
    date_released = models.DateField(blank=True)
    
    # The date and time this album was added to the database
    pub_date = models.DateTimeField(auto_now_add=True)
    
    # Whether this album appears on the website or not
    is_public = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s' % self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Album, self).save(*args, **kwargs)