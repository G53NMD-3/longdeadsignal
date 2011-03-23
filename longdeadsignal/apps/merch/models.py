from django.db import models

class Merch(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.PositiveIntegerField()
