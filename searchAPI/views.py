from rest_framework import viewsets
import requests
from searchAPI.models import YoutubeVideo
from searchAPI.serializers import YoutubeVideoSerializer

class YouTubeSearchVideoViewSet(viewsets.ModelViewSet):
    serializer_class = YoutubeVideoSerializer

    def get_queryset(self):
        return YoutubeVideo.objects.all()

    


