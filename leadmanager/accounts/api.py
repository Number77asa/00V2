from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, SocialSerializer
from . import serializers
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from social_core.backends.oauth import BaseOAuth2
from social_django.utils import load_strategy, load_backend
from requests.exceptions import HTTPError
from rest_framework import generics, permissions, status, views
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import login
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# we just created this seralizers.py file within this same directory
# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

# *args & &kwargs is a way python says it can take more arguments
    def post(self, request, *args, **kwargs):
        # request.data -> any data that comes in is going to get passed through this seraializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # we save user in database
        user = serializer.save()
        # finally we want send response back ; we pass in user object, and a method
        # the user is 1-1 with the token it gives, so when u make a request from front end
        # wheter its (postman, react, vue, angular) w/e and it can be used to login immediately;
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # needed to add teh [1] (different from brads..why?) --> The Token.objects.create returns a tuple (instance, token). just use the second position [1]
            "token": AuthToken.objects.create(user)[1]
        })

# Login API


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        # line below, get the data, pass the data in
        serializer = self.get_serializer(data=request.data)
        # check that data in is valid with the prebuilt module of rules that check if its valid
        serializer.is_valid(raise_exception=True)
        # the validated_data module validates the registered user in the registser-api above
        user = serializer.validated_data
        # the return for the method/function post above, will be same as registered user
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
# Get User API
# So permissions.isathen says: we want this route to be protected; needs a valid toek to access it


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer
# it will return whatever user is associated with that token

    def get_object(self):
        return self.request.user


class SocialLoginView(generics.GenericAPIView):
    """Log in using facebook"""
    serializer_class = serializers.SocialSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Authenticate user through the provider and access_token"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = serializer.data.get('provider', None)
        strategy = load_strategy(request)

        try:
            backend = load_backend(strategy=strategy, name=provider,
                                   redirect_uri=None)

        except MissingBackend:
            return Response({'error': 'Please provide a valid provider'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            if isinstance(backend, BaseOAuth2):
                access_token = serializer.data.get('access_token')
            user = backend.do_auth(access_token)
        except HTTPError as error:
            return Response({
                "error": {
                    "access_token": "Invalid token",
                    "details": str(error)
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        except AuthTokenError as error:
            return Response({
                "error": "Invalid credentials",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            authenticated_user = backend.do_auth(access_token, user=user)

        except HTTPError as error:
            return Response({
                "error": "invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        except AuthForbidden as error:
            return Response({
                "error": "invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        if authenticated_user and authenticated_user.is_active:
            # generate JWT token
            login(request, authenticated_user)
            data = {
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )}
            # customize the response to your needs
            response = {
                "email": authenticated_user.email,
                "username": authenticated_user.username,
                "token": data.get('token')
            }
            return Response(status=status.HTTP_200_OK, data=response)
