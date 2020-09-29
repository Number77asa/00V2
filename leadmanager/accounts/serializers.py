# want to be able to register a user atleast with postman
# django already has a user model, weree just using knox for tokens
from django.core.validators import validate_email
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication

from django.core.exceptions import ValidationError
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core import exceptions
from django.utils.translation import gettext as _
# User Serializer
# very similar to the lead searlizer we used

# from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
# at the same level as the class, we create a method here with define (def)
# this methdo creates the use r and returns it


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# Login Serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # the below comes from the prebuilt modueles in the authentication moduel; imported above.
        # e.g. is_active is a property of user, which are modules that are made for:
        # (django auth documentation, rest framework document, and knox documentat)
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class SocialSerializer(serializers.Serializer):

    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(
        max_length=4096, required=True, trim_whitespace=True)
