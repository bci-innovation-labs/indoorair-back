import csv
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import views, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from foundation.models import TimeSeriesDatum


class DownloadCSVReport01API(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        # https://docs.djangoproject.com/en/2.2/howto/outputting-csv/

        data = TimeSeriesDatum.objects.filter(
            sensor__name="Temperature",
            sensor__instrument__user=request.user,
        )

        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="temperature_data.csv"'

        # Connect our response object with our CSV writer object.
        writer = csv.writer(response)

        # This is the header row
        writer.writerow(['sensor_name', 'sensor_id', 'time', 'value',])

        # Let us go through all our data and generate our CSV file.
        for datum in data:
            writer.writerow([datum.sensor.name, datum.sensor.id, datum.time, datum.value])

        return response
