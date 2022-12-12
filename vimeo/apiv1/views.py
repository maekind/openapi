""" Specific view for API V1 """
import time
from rest_framework import generics

from .parser import Parser
from video.models import Video, Thumb, Owner, Quality, Seo
from video.serializers import VideoSerializer


class VideoDetailAPIView(generics.RetrieveAPIView):
    """
    Details of a video by primary key (RETRIEVE)
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_object(self):
        """ get object override for creating video into the database """

        if self.kwargs['pk'] is not None:

            try:
                pk = int(self.kwargs['pk'])
                if not Video.objects.filter(id=pk).exists():
                    print(f"Retrieving video data for new id {pk}")
                    start_time = time.time()
                    # Initializing parser with the video id
                    parser = Parser(pk)
                    # Trying to fetch video's json data
                    json_data = parser.fetch_data()

                    if json_data is not None and json_data != '':
                        # Create object in to the database before returning object
                        self._create_object(json_data)
                        print(
                            f"New object creation in {(time.time() - start_time):.2f} seconds")

            except Exception as ex:
                print(f"{ex}: Invalid id!")

        return super().get_object()

    def _create_object(self, data):
        """ Method to create new object """

        # TODO: Parse data before inserting.

        print("Creating object into the database ...", end="")
        video = Video.objects.create(
            id=data['video'].get('id'),
            title=data['video'].get('title'),
            duration=data['video'].get('duration'),
            height=data['video'].get('height'),
            width=data['video'].get('width'),
            fps=data['video'].get('fps')
        )

        if video is not None:
            # Creating thumbs
            thumbs = data['video'].get('thumbs')
            for key, value in thumbs.items():
                Thumb.objects.create(video=video, height=key, url=value)

            # Creating owner
            owner = data['video'].get('owner')
            Owner.objects.create(
                video=video,
                id=owner.get('id'),
                name=owner.get('name'),
                image=owner.get('img'),
                image_max=owner.get('img_2x'),
                url=owner.get('url'),
                account_type=owner.get('account_type'),
            )

            # Creating seo information
            seo = data['seo']
            Seo.objects.create(
                video=video, upload_date=seo.get('upload_date'),
                embeded_url=seo.get('embed_url'),
                description=seo.get('description'),
                thumbnail=seo.get('thumbnail'),
            )

            # Creating video qualities
            qualities = data['request']['files'].get('progressive')
            for value in qualities:
                Quality.objects.create(video=video,
                                       height=value.get('height'),
                                       width=value.get('width'),
                                       quality=value.get('quality'),
                                       fps=value.get('fps'),
                                       url=value.get('url'),
                                       mime_type=value.get('mime'),
                                       )

        print("OK")


video_detail_apiview = VideoDetailAPIView.as_view()
