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

class PostCateMVS(viewsets.ModelViewSet):
    serializers_class = PostCateSerializers

    def get_serializer(self, *args, **kwargs):
        pass

    def get_serializer_class(self):
        pass
    
    @action(methods=['GET'], detail = False, url_path='post_cate_get_all_api', url_name='post_cate_get_all_api')
    def post_cate_get_all_api(self, request, *args, **kwargs):
        queryset = PostCate.objects.all()
        serializers = self.serializers_class(queryset)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail = False, url_path='post_cate_add_api', url_name='post_cate_add_api')
    def post_cate_add_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializers_class(data=request.data)
            if serializers.is_valid():
                model = serializers.add(request)
                if model:
                    data = {}
                    data['message'] = 'Add successfully!'
                    return Response(data=data, status=status.HTTP_201_CREATED)
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("PostCateMVS_add_api: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['PATCH'], detail=False, url_path='post_cate_update_api', url_name='post_cate_update_api')
    def post_cate_update_api(self, request, *args, **kwargs):
        try:
            serializer = self.serializers_class(data=request.data)
            print(serializer)
            if serializer.is_valid():
                print(request)
                model = serializer.update(request)
                print(model)
                if model:
                    data = {}
                    data['message'] = 'Update successfully!'
                    return Response(data=data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PostCate.DoesNotExist:
            return Response({'error': 'PostCate not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            print("PostCateMVS_edit_api_error: ", error)
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)



class PostIndexMVS(viewsets.ModelViewSet):
    serializer_class = PostIndexSerializers

    def get_queryset(self):
        return PostIndex.objects.all() 
    
    @action(methods=['GET'], detail=False, url_path='post_index_get_all_api', url_name='post_index_get_all_api')
    def post_index_get_all_api(self, request, *args, **kwargs):
        queryset = PostIndex.objects.all()
        serializers = self.serializer_class(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)