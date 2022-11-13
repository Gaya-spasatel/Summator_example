from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Summator
from .serializers import SummatorSerializer
import summary


class SummatorView(APIView):

    def get(self, request, a, b):
        summator = Summator(a, b, summary.summary(a, b))

        serializer_for_request = SummatorSerializer(instance=summator)

        return Response(serializer_for_request.data)
