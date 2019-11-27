from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(
         validators=[
             UniqueValidator(queryset=User.objects.all())
         ]
    )
    username = serializers.CharField(
         validators=[
             UniqueValidator(queryset=User.objects.all())
         ]
    )
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')

        # This is for debugging purposes only.
        print(first_name, last_name, username, email, password)

        # Plug in our data from the request into our `User` model.
        user = User.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()

        return user
