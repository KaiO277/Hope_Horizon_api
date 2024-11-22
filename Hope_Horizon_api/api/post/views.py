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

class CourseRegisterWebinarPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        next_page = previous_page = None
        if self.page.has_next():
            next_page = self.page.next_page_number()
        if self.page.has_previous():
            previous_page = self.page.previous_page_number()
        return Response({
            'totalRows': self.page.paginator.count,
            'page_size': self.page_size,
            'current_page': self.page.number,
            'next_page': next_page,
            'previous_page': previous_page,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'data': data,
        })

class PostCateMVS(viewsets.ModelViewSet):
    serializer_class = PostCateSerializers  
    permission_classes = [IsAuthenticated]
    pagination_class = CourseRegisterWebinarPagination

    @action(methods=['GET'], detail=False, url_name='post_cate_get_all_api', url_path='post_cate_get_all_api')
    def post_cate_get_all_api(self, request, *args, **kwargs):
        queryset = PostCate.objects.all()
        serializers = self.serializer_class(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    @action(methods=['GET'], detail=False, url_path='post_cate_get_list_page_all_api', url_name='post_cate_get_list_page_all_api')
    def post_cate_get_list_page_all_api(self, request, *args, **kwargs):
        queryset = PostCate.objects.all()
        paginator = CourseRegisterWebinarPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        if paginated_queryset is not None:
            serializer = self.serializer_class(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail = False, url_path='post_cate_add_api', url_name='post_cate_add_api')
    def post_cate_add_api(self, request, *args, **kwargs):
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
            print("PostCateMVS_add_api: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['PATCH'], detail=False, url_path='post_cate_update_api', url_name='post_cate_update_api')
    def post_cate_update_api(self, request, *args, **kwargs):
        try:
            serializer = self.serializers_class(data=request.data)
            # print(serializer)
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
        
    @action(methods=['DELETE'], detail=False, url_path='post_cate_delete_api', url_name='post_cate_delete_api')
    def post_cate_delete_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializers_class(data=request.data)
            if serializers.is_valid():
                data = {}
                result = serializers.delete(request)
                if result:
                    data['message'] = 'Delete successfully!'
                    return Response(data=data, status=status.HTTP_204_NO_CONTENT)
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("PostCateMVS_delete_api_error: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

class PostAuthorMVS(viewsets.ModelViewSet):
    serializer_class = PostAuthorSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = CourseRegisterWebinarPagination

    @action(methods=['POST'], detail=False, url_name='post_author_add_api', url_path='post_author_add_api')
    def post_author_add_api(self, request, *args, **kwargs):
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
            print("PostAuthorMVS_add_api: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['GET'], detail=False, url_name='post_author_get_all_api', url_path='post_author_get_all_api')
    def post_author_get_all_api(self, request, *args, **kwargs):
        queryset = PostAuthor.objects.all()
        serializers = self.serializer_class(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)   

    @action(methods=['GET'], detail=False, url_name='post_author_get_list_page_all_api', url_path='post_author_get_list_page_all_api')
    def post_author_get_list_page_all_api(self, request, *args, **kwargs):
        queryset = PostAuthor.objects.all()
        paginator = CourseRegisterWebinarPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        if paginated_queryset is not None:
            serializer = self.serializer_class(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='post_author_get_by_id_api', url_name='post_author_get_by_id_api')
    def post_author_get_by_id_api(self, request, *args, **kwargs):
        try:
            post_author_id = kwargs['id']
            if post_author_id == 0:
                return Response(data={}, status=status.HTTP_200_OK)
            queryset = PostAuthor.objects.get(pk = post_author_id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("PostAuthorMVS_get_by_id_api_error: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PATCH'], detail=False, url_name='post_author_update_api', url_path='post_author_update_api')
    def post_author_update_api(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data= request.data)
            if serializer.is_valid():
                model = serializer.update(request)
                if model:
                    data = {}
                    data['message'] = 'Update successfully!'
                    return Response(data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("PostAuthorMVS_update_api_error: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['DELETE'], detail=False, url_path='post_author_delete_api', url_name='post_author_delete_api')
    def post_author_delete_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializer_class(data=request.data)
            if serializers.is_valid():
                data = {}
                result = serializers.delete(request)
                if result:
                    data['message'] = 'Delete successfully!'
                    return Response(data=data, status=status.HTTP_204_NO_CONTENT)
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("PostAuthorMVS_delete_api_error: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

#done
class PostIndexMVS(viewsets.ModelViewSet):
    serializer_class = PostIndexSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PostIndex.objects.all() 
    
    @action(methods=['GET'], detail=False, url_name='post_index_get_all_api', url_path='post_index_get_all_api')
    def post_index_get_all_api(self, request, *args, **kwargs):
        queryset = PostIndex.objects.all()
        serializers = self.serializer_class(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    
    @action(methods=['GET'], detail=False, url_path='post_index_get_list_page_all_api', url_name='post_index_get_list_page_all_api')
    def post_index_get_list_page_all_api(self, request, *args, **kwargs):
        queryset = PostIndex.objects.all()
        paginator = CourseRegisterWebinarPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        if paginated_queryset is not None:
            serializer = self.serializer_class(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['GET'], detail=False, url_name='post_index_get_all_by_post_cate_id_api', url_path='post_index_get_all_by_post_cate_id_api')
    def post_index_get_all_by_post_cate_id_api(self, request, *args, **kwargs):
        post_cate_id = kwargs['post_cate_id']
        if post_cate_id == 0:
            return Response(data={}, status=status.HTTP_200_OK)
        query = Q(post_cate__id = post_cate_id)
        queryset = PostIndex.objects.filter(query)
        serializer = self.serializer_class(queryset, many=True, context={"request":request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail=False, url_name='post_index_add_api', url_path='post_index_add_api')
    def post_index_add_api(self, request, *args, **kwargs):
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
            print("PostIndexMVS_add_api: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['DELETE'], detail=False, url_name='post_index_delete_api', url_path='post_index_delete_api')
    def post_index_delete_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializer_class(data=request.data)
            if serializers.is_valid():
                data = {}
                result = serializers.delete(request)
                if result:
                    data['message'] = 'Delete successfully!'
                    return Response(data=data, status=status.HTTP_204_NO_CONTENT)
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("PostindexMVS_delete_api_error: ", error)
        return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PATCH'], detail=False, url_name='post_index_update_api', url_path='post_index_update_api')
    def post_index_update_api(self, request, *args, **kwargs):
        try:
            serializers = self.serializer_class(data=request.data)
            if serializers.is_valid():
                model = serializers.update(request)
                if model:
                    data = {}
                    data['message'] = 'Update successfully!'
                    return Response(data=data, status=status.HTTP_200_OK)
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("PostIndexMVS_update_api: ", error)
            return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)