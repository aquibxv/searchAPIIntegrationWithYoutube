from rest_framework import viewsets
from searchAPI.models import YoutubeVideo
from searchAPI.serializers import YoutubeVideoSerializer
import logging

logger = logging.getLogger(__name__)

class YouTubeGetStoredVideosViewSet(viewsets.ModelViewSet):
    """
    ViewSet for retrieving stored YouTube videos.

    This class extends the `viewsets.ModelViewSet` class and allows for the retrieval of stored YouTube videos using a
    REST API. It uses the `YoutubeVideoSerializer` class to serialize the videos and allows for sorting the results by
    `publish_time` in descending order.

    """
    serializer_class = YoutubeVideoSerializer  # Serializer to use for the videos

    def get_queryset(self):
        """
        Return the queryset of all YouTube videos.
        """
        logger.info("Recived A Request for reteriving the Youtube Videos Stored Data")
        return YoutubeVideo.objects.all().order_by('-publish_time')

        

    


