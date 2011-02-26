from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
    """
    A Post is a single article or message containing an update which readers
    of the website would find interesting.
    """
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)
    
    tease_markdown = models.TextField(blank=True)
    tease_html = models.TextField(blank=True)
    
    body_markdown = models.TextField(blank=True)
    body_html = models.TextField(blank=True)
    
    author = models.ForeignKey('auth.user')
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s' % self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('news:post_detail', [self.slug])