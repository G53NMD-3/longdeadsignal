from django.views.generic import FormView, UpdateView, CreateView
from longdeadsignal.apps.news.models import Post
from longdeadsignal.apps.news.forms import PostForm
from longdeadsignal.apps.merch.models import Merch
from longdeadsignal.apps.merch.forms import MerchForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import copy

class PostBadminEditView(FormView):
    model=Post
    form_class=PostForm
    template_name='badmin/news/post_form.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostBadminEditView, self).dispatch(*args, **kwargs)

class PostBadminUpdateView(PostBadminEditView, UpdateView):
    def get_success_url(self):
        return reverse('badmin:news:post_list')

class PostBadminCreateView(PostBadminEditView, CreateView):
    def form_valid(self, form):
        """Set the post author as the logged in user"""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostBadminCreateView, self).form_valid(form)
        

class MerchBadminEditView(FormView):
    model=Merch
    form_class=MerchForm
    template_name='badmin/merch/merch_form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MerchBadminEditView, self).dispatch(*args, **kwargs)

class MerchBadminUpdateView(MerchBadminEditView, UpdateView):
    pass
    # def get_success_url(self):
    #     return reverse('badmin:merch:merch_list')

class MerchBadminCreateView(MerchBadminEditView, CreateView):
    pass