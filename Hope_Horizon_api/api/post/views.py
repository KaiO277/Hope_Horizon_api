from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q, Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.forms.models import model_to_dict
import re
from rest_framework.parsers import MultiPartParser, FormParser

from api.models import *
from .serializers import *
# from api import status_http

class PostIndexMVS(viewsets.ModelViewSet):
    serializer_class = PostIndexSerializers

    def get_queryset(self):
        return PostIndex.objects.all() 
    
    @action(methods=['GET'], detail=False, url_path='post_index_get_all_api', url_name='post_index_get_all_api')
    def post_index_get_all_api(self, request, *args, **kwargs):
        queryset = PostIndex.objects.all()
        serializers = self.serializer_class(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

