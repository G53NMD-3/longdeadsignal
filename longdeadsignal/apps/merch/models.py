from django.db import models
from django.template.defaultfilters import slugify

class Merch(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(db_index=True, editable=False, unique=True)
    price = models.PositiveIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s' % self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Merch, self).save(*args, **kwargs)
    