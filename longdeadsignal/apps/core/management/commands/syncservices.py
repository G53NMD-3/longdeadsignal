from django.core.management.base import NoArgsCommand
from syncr.app.youtube import YoutubeSyncr
from syncr.app.tweet import TwitterSyncr
from syncr.app.flickr import FlickrSyncr
from django.conf import settings
from flickrapi.exceptions import FlickrError

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        if settings.SYNC_TWITTER:
            # Gets the latest 20 tweets (API limitation) by the user
            TwitterSyncr(None, None)\
                .syncTwitterUserTweets(settings.TWITTER_USERNAME)
        
        if settings.SYNC_YOUTUBE:
            # Syncs all videos uploads by the user
            YoutubeSyncr().syncUserUploads(settings.YOUTUBE_USERNAME)
        
        if settings.SYNC_FLICKR and settings.FLICKR_API_KEY and \
            settings.FLICKR_SECRET:
            print settings.FLICKR_USERNAME
            # Syncs all (could take a while) videos by the user
            try:
                FlickrSyncr(settings.FLICKR_API_KEY, settings.FLICKR_SECRET)\
                    .syncAllPublic(settings.FLICKR_USERNAME)
            except FlickrError, e:
                # Most likely this will fail because the username does not
                # exist
                print 'Flickr Error'
                print e
                pass