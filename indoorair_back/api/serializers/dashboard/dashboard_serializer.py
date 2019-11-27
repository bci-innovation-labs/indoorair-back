import statistics
from rest_framework import serializers

from foundation.models import TimeSeriesDatum, Sensor


class DashboardSerializer(serializers.BaseSerializer):
    def get_values(self, sensor_name, instrument):
        sensor = Sensor.objects.get(
             name=sensor_name,
             instrument=instrument,
        )
        values = TimeSeriesDatum.objects.filter(sensor=sensor).values_list('value', flat=True)
        return values

    def get_statistics(self, values):
        try:
            mean = statistics.mean(values)
        except Exception as e:
            mean = "NF"
        try:
            median = statistics.median(values)
        except Exception as e:
            median = "NF"
        try:
            mode = statistics.mode(values)
        except Exception as e:
            mode = "NF"
        return {
            'mean': mean,
            'median': median,
            'mode': mode
        }

    def to_representation(self, instruments):
        """
        Get the list of instruments and perform our computations.
        """
        results = []
        for instrument in instruments:
            temp_values = self.get_values("Temperature", instrument)
            hum_values = self.get_values("Humidity", instrument)
            pressure_values = self.get_values("Pressure", instrument)
            co2_values = self.get_values("Co2", instrument)
            tvoc_values = self.get_values("TVOC", instrument)

            results.append({
                'id': instrument.id,
                'name': instrument.name,
                'temperature': self.get_statistics(temp_values),
                'humidity': self.get_statistics(hum_values),
                'pressure': self.get_statistics(pressure_values),
                'co2': self.get_statistics(co2_values),
                'tvoc': self.get_statistics(tvoc_values),
            })
        return {
            'results': results,
            'count': instruments.count()
        }
