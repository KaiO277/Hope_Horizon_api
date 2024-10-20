from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group, Permission
from django.db.models import Q
from collections import OrderedDict
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta, datetime
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests, os
from django.http import FileResponse, HttpResponse
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from django.contrib.auth.decorators import login_required
import hashlib
import urllib.parse

from .serializers import *
from . import status_http
from .models import *

# Create your views here.

class GoogleView(APIView):
    def post(self, request):

        s = Setting.objects.first()
        if s and s.is_lock_login:
            content = {
                'message': 'Không thể đăng nhập lúc này'}
            return Response(content)

        email = request.data.get("email")
        print("GoogleView_email: ", email)
        payload = {'access_token': request.data.get(
            "token_google")}  # validate the token
        r = requests.get(
            'https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {
                'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        print("GoogleView_data: ", data)

        email = data["email"]
        # create user if not exist
        print(email)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print("GoogleView_User.DoesNotExist")
            # token_google = request.data.get("token_google")
            # avatar = request.data.get("imageUrl")
            first_name = request.data.get("givenName")
            last_name = request.data.get("familyName")
            user = User()
            user.username = email
            # provider random default password
            user.password = make_password(
                BaseUserManager().make_random_password())
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()

        # generate token without username & password
        token = RefreshToken.for_user(user)
        response = {}
        response['access'] = str(token.access_token)
        response['refresh'] = str(token)
        return Response(response)

# class GoogleView(APIView):
#     def post(self, request):
#         s = Setting.objects.first()
#         if s and s.is_lock_login:
#             return Response({'message': 'Không thể đăng nhập lúc này'})

#         token = request.data.get("token_google")
#         print("Received token:", token)

#         payload = {'access_token': token}
#         r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        
#         print("Google API response:", r.text)  # Ghi log phản hồi từ Google
        
#         data = r.json()  # Chuyển đổi phản hồi thành JSON
#         if 'error' in data:
#             return Response({'message': 'wrong google token / this google token is already expired.'})

#         email = data.get("email")
#         if not email:
#             return Response({'message': 'Email not found in Google token data.'})

#         print("GoogleView email:", email)

#         # Tạo người dùng nếu không tồn tại
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             first_name = data.get("given_name")
#             last_name = data.get("family_name")
#             user = User()
#             user.username = email
#             user.password = make_password(BaseUserManager().make_random_password())
#             user.email = email
#             user.first_name = first_name
#             user.last_name = last_name
#             user.save()

#         token = RefreshToken.for_user(user)
#         response = {
#             'access': str(token.access_token),
#             'refresh': str(token)
#         }
#         return Response(response)
