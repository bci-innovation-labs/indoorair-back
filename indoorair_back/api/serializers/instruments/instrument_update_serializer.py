from rest_framework import serializers


class InstrumentUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    location = serializers.CharField(required=True)

    def update(self, object, validated_data):
        name = validated_data.get('name', None)
        location = validated_data.get('location', None)
        object.name = name
        object.location = location
        object.save()

        return object
