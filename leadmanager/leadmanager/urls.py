"""leadmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import include
from django.conf import settings
from django.urls import path
#from django.contrib import admin
from django.urls import path, include
#from django.views.generic import TemplateView

# from django.contrib.auth.views import login

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
    path('', include('accounts.urls')),
    # path('', TemplateView.as_view(
    #    template_name='../../frontend/templates/frontend/social_app/index.html')),

    #path('admin/', admin.site.urls),
    # perhaps '' is necearry
    path('api/auth/', include('rest_framework_social_oauth2.urls')),
    # accounts above is currenlty an app, here its just a directory
    #path('accounts/', include('allauth.urls')),

]
