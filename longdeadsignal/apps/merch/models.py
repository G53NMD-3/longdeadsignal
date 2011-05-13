from django.db import models
from django.template.defaultfilters import slugify

class Merch(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(db_index=True, editable=False, unique=True)
    price = models.PositiveIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="merch")
    
    def __unicode__(self):
        return u'%s' % self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('merch:merch_detail', (), {'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Merch, self).save(*args, **kwargs)
    