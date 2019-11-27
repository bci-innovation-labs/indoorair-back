"""
homepage/views.py
"""
from rest_framework import status, views, response


class VersionAPI(views.APIView):    
    def get(self, request):
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'version': '3',
            }
        )
