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
from api import status_http

class PodcastCateMVS(viewsets.ModelViewSet):
    serializer_class = PodcastCateSerializers

    def get_queryset(self):
        return PodcastCate.objects.all() 
    
    @action(methods=['GET'], detail=False, url_path='podcast_cate_get_all_api', url_name='podcast_cate_get_all_api')
    def podcast_cate_get_all_api(self, request, *args, **kwargs):
        queryset = PodcastCate.objects.all()
        serializers = self.serializer_class(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail=False, url_path='podcast_cate_add_api', url_name='podcast_cate_add_api')
    def podcast_cate_add_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializer_class(data=request.data)
            if serializers.is_valid():
                model = serializers.add(request)
                if model:
                    data = {}
                    data['message'] = 'Add successfully'
                    return Response(data=data, status=status.HTTP_201_CREATED)
            return Response(data=serializers.error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("PodcastCateMVS_add_api: ", e)
        return Response({'error': 'Bad request'}, status = status.HTTP_BAD_REQUEST)

