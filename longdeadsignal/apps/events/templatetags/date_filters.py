from django import template
from django.utils.timesince import timesince
import datetime

register = template.Library()

def timetill(value):
    if value is None:
        return ''
    now = datetime.datetime.now()
    return timesince(now - (value - now))

register.filter('timetill', timetill)