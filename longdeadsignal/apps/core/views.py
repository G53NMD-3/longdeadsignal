from django.views.generic import TemplateView
from syncr.youtube.models import Video
from syncr.flickr.models import Photo
from longdeadsignal.apps.news.models import Post
from longdeadsignal.apps.events.models import Event
import operator
import datetime

class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'
    
    def render_to_response(self, context, *args, **kwargs):
        # Get all of the different things from the database which will be in
        # the list of new stuff on the home page.
        video_list = Video.objects.order_by('-published')[:10]
        photo_list = Photo.objects.order_by('-upload_date')[:10]
        post_list = Post.objects.order_by('-pub_date')[:10]
        
        # Put them all into a single list
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
        
        # Sort the list based upon the time each was added
        latest_things = sorted(latest_things, key=operator.itemgetter('pub_date'), reverse=True)
        
        # Put the list of new things into the context
        context['latest_things'] = latest_things
        
        # Put the upcomming events in the context
        context['upcomming_events'] = Event.objects.filter(date__gte=datetime.datetime.now()).order_by('date')[:5]
        
        return super(IndexTemplateView, self).render_to_response(context, *args, **kwargs)