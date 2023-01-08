from rest_framework import viewsets
from searchAPI.models import YoutubeVideo
from searchAPI.serializers import YoutubeVideoSerializer

class YouTubeGetStoredVideosViewSet(viewsets.ModelViewSet):
    serializer_class = YoutubeVideoSerializer

    def get_queryset(self):
        return YoutubeVideo.objects.all()

    class Meta:
        ordering = ('-publish_time')
        

    


