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
    permission_classes = [IsAuthenticated]

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
    
    @action(methods=['PATCH'], detail=False, url_path='podcast_cate_update_api', url_name='podcast_cate_update_api')
    def podcast_cate_update_api(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                model = serializer.update(request)
                if model:
                    data = {}
                    data['message'] = 'Update successfully!'
                    return Response(data=data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("PodcastCateMVS_update_api: ", e)
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['DELETE'], detail=False, url_path='podcast_cate_delete_api', url_name='podcast_cate_delete_api')
    def podcast_cate_delete_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializer_class(data=request.data)
            if serializers.is_valid():
                data = {}
                result = serializers.delete(request)
                if result:
                    data['message'] = 'Delete successfully!'
                    return Response(data=data, status=status.HTTP_204_NO_CONTENT)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("PodcastCateMVS_delete_api_error: ", e)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
class PodcastAuthorMVS(viewsets.ModelViewSet):
    serializer_class = PodcastAuthorSerializers
    permission_classes = [IsAuthenticated]
    
    @action(methods=['GET'], detail=False, url_name='podcast_author_get_all_api', url_path='podcast_author_get_all_api')
    def podcast_author_get_all_api(self, request, *args, **kwargs):
        queryset = PodcastAuthor.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail=False, url_name='podcast_author_add_api', url_path='podcast_author_add_api')
    def podcast_author_add_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializer_class(data=request.data)
            if serializers.is_valid():
                model = serializers.add(request)
                if model:
                    data = {}
                    data['message'] = 'Add successfully!'
                    return Response(data=data, status=status.HTTP_201_CREATED)
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("PodcastAuthorMVS_add_api_error: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['PATCH'], detail=False, url_name='podcast_author_update_api', url_path='podcast_author_update_api')
    def podcast_author_update_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializer_class(data=request.data)
            if serializers.is_valid():
                model = serializers.update(request)
                if model:
                    data = {}
                    data['message'] = 'Update successfully!'
                    return Response(data=data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("PodcastAuthorMVS_update_api_error: ", e)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['DELETE'], detail=False, url_name='podcast_author_delete_api', url_path='podcast_author_delete_api')
    def podcast_author_delete_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializer_class(data=request.data)
            if serializers.is_valid():
                data = {}
                result = serializers.delete(request)
                if result:
                    data['message'] = 'Delete successfully!'
                    return Response(data=data, status=status.HTTP_204_NO_CONTENT)
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("PodcastAuthorMVS_delete_api_error: ", e)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
class PodcastIndexMVS(viewsets.ModelViewSet):
    serializer_class = PodcastIndexSerializers
    permission_classes = [IsAuthenticated]

    @action(methods=['GET'], detail=False, url_name='podcast_index_get_all_api', url_path='podcast_index_get_all_api')
    def podcast_index_get_all_api(self, request, *args, **kwargs):
        queryset = PodcastIndex1.objects.all()
        serializers = self.serializer_class(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    
