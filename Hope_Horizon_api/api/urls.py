from django.conf.urls import include
from django.urls import path

from rest_framework import permissions

from .serializers import MyTokenObtainPairView
from .views import *

urlpatterns = [
    #
    path('post/', include('api.post.urls')),
    path('try/', include('api.try.urls')),

    #
    path('auth/google/', GoogleView.as_view(), name='google'),
    path('auth/login/', MyTokenObtainPairView.as_view()),
]
