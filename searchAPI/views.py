from rest_framework import viewsets
from searchAPI.models import YoutubeVideo
from django.db.models import Q
from searchAPI.serializers import YoutubeVideoSerializer
from functools import reduce
import operator
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


class SearchYoutubeVideosAPIViewSet(viewsets.ModelViewSet):
    """
    A viewset for searching for YouTube videos based on their title and description.
    """
    serializer_class = YoutubeVideoSerializer
    """The serializer class to use for this viewset."""

    def get_queryset(self):
        """
        Retrieve the queryset for this viewset.

        The queryset consists of YouTube videos that contain the specified `title` and `description`
        in their title and description fields, respectively. If either `title` or `description` is not
        specified, it defaults to an empty string. The search is case-insensitive and uses the `icontains`
        lookup. The queryset is then ordered by `publish_time` in descending order.

        Note:
        The queryset can be improved by using Full-text search indexes to significantly improve the
        performance of queries that use the `icontains` lookup to search for string patterns. We can
        use the `SearchVector` and `SearchQuery` to achieve this. However, for simplicity, this
        implementation uses a SQLite database.
        """    
        title = self.request.query_params.get('title')
        if title is not None:
            title = " ".join(title.split())
            title = title.split(" ")
        else:
            title = [""]

        description = self.request.query_params.get('description')
        if description is not None:
            description = " ".join(description.split())
            description = description.split(" ")
        else:
            description = [""]
    
        query_title = reduce(operator.or_,(Q(title__icontains=word) for word in title))
        query_decription = reduce(operator.or_,(Q(description__icontains=word) for word in description))

        queryset = YoutubeVideo.objects.filter(query_title | query_decription).order_by('-publish_time')
        return queryset


        

    


