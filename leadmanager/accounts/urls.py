
from django.urls import path, include

from django.conf.urls import url, include
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
# from .api import SocialLoginView
from .views import SocialLoginView
from rest_framework import routers
router = routers.DefaultRouter()
# from rest_framework import routers
# import views
urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    # the endpoint below destroys the token
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    # path('api/auth', include('rest_framework_social_oauth2.urls')),

    path('api/auth/register2', SocialLoginView.as_view()),
    # note obtaintoken method was just imported in serializers; nothing more
    # path('api/auth/register3', ObtainAuthToken.as_view()),
    # url(r'^login/(?P<backend>[\w-]+)$', ObtainAuthToken.as_view(), ), #google wants this one?

    # url(r'^oauth2/google/$', views.oauth2_google),
    # path('api/auth/register3', oauth2_google.as_view()),
    # path('api/auth/register3', ObtainAuthToken.as_view()),
    # path('', include(router.urls)),
    #    path('social-auth/', SocialSignUp.as_view()),
]
