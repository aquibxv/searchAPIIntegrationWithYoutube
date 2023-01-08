from rest_framework import serializers
from searchAPI.models import YoutubeVideo

class YoutubeVideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the `YoutubeVideo` model.

    This class extends the `serializers.ModelSerializer` class and serializes the fields of the `YoutubeVideo` model for
    use in a REST API.
    """
    class Meta:
        model = YoutubeVideo  # The model to serialize
        fields = '__all__'  # Serialize all fields of the model
