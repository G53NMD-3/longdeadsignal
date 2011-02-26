from django.views.generic import UpdateView
from longdeadsignal.apps.news.models import Post
from longdeadsignal.apps.news.forms import PostForm
from django.core.urlresolvers import reverse

class PostBadminUpdateView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='badmin/news/post_form.html'
    
    def get_success_url(self):
        return reverse('badmin:news:post_list')