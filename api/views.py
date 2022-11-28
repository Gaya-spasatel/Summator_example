from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Summator, ImageFromPillow
from .serializers import SummatorSerializer, ImageFromPillowSerializer
import summary
import time


class SummatorView(APIView):

    def get(self, request, a, b):
        summator = Summator(a, b, summary.summary(a, b))

        serializer_for_request = SummatorSerializer(instance=summator)

        return Response(serializer_for_request.data)


class ImageFromPillowView(APIView):

    def get(self, request):
        ts = str(time.time()).replace('.', '_')
        image_path = f"/app/images_bin/{ts}.jpg"
        summary.generate_img(image_path)
        image_string = summary.encode_image(image_path)

        image_result = ImageFromPillow(image_string, 'utf-8')
        serializer_for_request = ImageFromPillowSerializer(instance=image_result)

        return Response(serializer_for_request.data)
