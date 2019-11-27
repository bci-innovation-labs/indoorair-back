from rest_framework import response, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from foundation.models import Instrument
from api.serializers import DashboardSerializer


class DashboardAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        print("DashboardAPI: user:", request.user)
        instruments = Instrument.objects.filter(user=request.user)
        serializer = DashboardSerializer(instruments)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
