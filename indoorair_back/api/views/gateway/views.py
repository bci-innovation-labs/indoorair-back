"""
gateway/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login, logout
from rest_framework import views, status, response

from api.serializers import RegisterSerializer, LoginSerializer


class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data,
        )


def post_logout_api(request):
    try:
        logout(request)
        return JsonResponse({
             "was_logged_out": True,
             "reason": None,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
             "was_logged_out": False,
             "reason": str(e),
        })
