from rest_framework import serializers
from searchAPI.models import YoutubeVideo


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = '__all__'