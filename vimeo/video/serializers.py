"""
Video serializers
"""

from rest_framework import serializers

from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    """ Video serializer """
    class Meta:
        """ Meta class for the serializer """
        model = Video
        fields = [
            'id',
            'title',
            'height',
            'width',
            'fps'
        ]
