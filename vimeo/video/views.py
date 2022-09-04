from rest_framework import generics

from .models import Video
from .serializers import VideoSerializer


class VideoListCreateAPIView(generics.ListCreateAPIView):
    """
    Video's list and creation interface (CREATE)
    """
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer
    # pagination_class = SmallResultsSetPagination

    # def perform_create(self, serializer):
    #     serializer.save()

    #     # Reload cache
    #     reboot_cache_main()


video_create_apiview = VideoListCreateAPIView.as_view()
