from django.views.generic import TemplateView
from syncr.youtube.models import Video
from syncr.flickr.models import Photo
from longdeadsignal.apps.news.models import Post
import operator

class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'
    
    def render_to_response(self, context, *args, **kwargs):
        video_list = Video.objects.order_by('-published')[:10]
        photo_list = Photo.objects.order_by('-upload_date')[:10]
        post_list = Post.objects.order_by('-pub_date')[:10]
        
        latest_things = []
        latest_things.extend({
            'type': 'video',
            'object': video,
            'pub_date': video.published,
        } for video in video_list)
        latest_things.extend({
            'type': 'photo',
            'object': photo,
            'pub_date': photo.upload_date,
        } for photo in photo_list)
        latest_things.extend({
            'type': 'post',
            'object': post,
            'pub_date': post.pub_date,
        } for post in post_list)
        
        latest_things = sorted(latest_things, key=operator.itemgetter('pub_date'), reverse=True)
        context['latest_things'] = latest_things
        return super(IndexTemplateView, self).render_to_response(context, *args, **kwargs)