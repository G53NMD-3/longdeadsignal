from django import forms
from longdeadsignal.apps.news.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)