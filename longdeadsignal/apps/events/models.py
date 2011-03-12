from django.db import models
from wmd import models as wmd_models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify
import datetime
import markdown

LOCATION_COUNTRY_DEFAULT = 'United Kingdom'

class Event(models.Model):
    # The title of the venue
    title = models.CharField('Event Title', max_length=100)
    slug = models.SlugField(unique=True, editable=False)
    
    # Location of the event
    location_title = models.CharField('Establishment', blank=True, max_length=100)
    
    location_address_1 = models.CharField('Address Line 1', blank=True, max_length=100)
    location_address_2 = models.CharField('Address Line 2', blank=True, max_length=100)
    location_address_3 = models.CharField('Address Line 3', blank=True, max_length=100)
    
    location_city = models.CharField('City', blank=True, max_length=100)
    location_post_code = models.CharField('Post Code', blank=True, max_length=100)
    location_country = models.CharField('Country', blank=True, max_length=100, default=LOCATION_COUNTRY_DEFAULT)
    
    # The location for google maps
    location_google_maps = models.CharField(blank=True, max_length=100)
    
    # The date and time of the event
    date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    
    # Before the event has taken place, a hype message from the band
    pre_event_message_markdown = wmd_models.MarkDownField('Pre event message', blank=True)
    pre_event_message_html = models.TextField(blank=True, editable=False)
    
    # After the event has taken place, a thankyou message from the band
    post_event_message_markdown = wmd_models.MarkDownField('Post event message', blank=True)
    post_event_message_html = models.TextField(blank=True, editable=False)
    
    # A list of videos and images related to the event
    media = models.ManyToManyField('events.EventMediaItem', blank=True)
    
    # System stuff
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date',)
        get_latest_by = 'pub_date'
    
    def __unicode__(self):
        return '%s %s' % (self.title, self.date)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.pre_event_message_html = markdown.markdown(self.pre_event_message_markdown)
        self.post_event_message_html = markdown.markdown(self.post_event_message_markdown)
        super(Event, self).save(*args, **kwargs)

class EventMediaItem(models.Model):
    # Generic Foreign Key
    # This is intented to point to a Video or Image
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')