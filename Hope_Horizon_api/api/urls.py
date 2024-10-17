from django.conf.urls import include
from django.urls import path

from rest_framework import permissions

# from .serializers import MyTokenObtainPairView
from .views import *

urlpatterns = [
    #
    path('post/', include('api.post.urls')),
]
