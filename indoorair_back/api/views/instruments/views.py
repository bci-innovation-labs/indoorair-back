"""
instrument/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from foundation.models import Instrument
from rest_framework import status, response, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api.serializers import InstrumentRetrieveSerializer
from api.serializers import InstrumentListSerializer
from api.serializers import InstrumentUpdateSerializer


class InstrumentListAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        instruments = Instrument.objects.filter(user=request.user)
        serializer = InstrumentListSerializer(instruments, many=True)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data,
        )


class InstrumentRetrieveAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get(self, request, id):
        instrument = Instrument.objects.get(id=int(id))
        serializer = InstrumentRetrieveSerializer(instrument, many=False)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class InstrumentUpdateAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def put(self, request, id):
        instrument = Instrument.objects.get(id=id)
        serializer = InstrumentUpdateSerializer(instrument, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'Updated instrument'
            }
        )
