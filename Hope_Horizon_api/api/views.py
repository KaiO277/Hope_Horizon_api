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
        # Check if login is locked
        s = Setting.objects.first()
        if s and s.is_lock_login:
            return Response({'message': 'Cannot login at this time'}, status=status.HTTP_403_FORBIDDEN)

        token_google = request.data.get("token_google")
        if not token_google:
            return Response({'message': 'Missing token'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify token with Google
        google_verification_url = f"https://oauth2.googleapis.com/tokeninfo?id_token={token_google}"
        google_response = requests.get(google_verification_url)
        google_data = google_response.json()

        # Handle invalid or expired token
        if google_response.status_code != 200 or 'error' in google_data:
            return Response({'message': 'wrong google token / this google token is already expired.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Extract email from Google's verified data
        email = google_data.get("email")
        if not email:
            return Response({'message': 'Email not found in Google token'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if user exists, otherwise create a new user
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            first_name = google_data.get("given_name", "")
            last_name = google_data.get("family_name", "")
            user = User(
                username=email,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(BaseUserManager().make_random_password())  # Random password
            )
            user.save()

            # Add user to 'MEMBER' group
            # member_group = Group.objects.get(name=settings.GROUP_NAME['MEMBER'])
            # member_group.user_set.add(user)

        # Generate JWT tokens for the user
        token = RefreshToken.for_user(user)
        return Response({
            'access': str(token.access_token),
            'refresh': str(token)
        }, status=status.HTTP_200_OK)

# class GoogleView(APIView):
#     def post(self, request):
#         s = Setting.objects.first()
#         if s and s.is_lock_login:
#             return Response({'message': 'Không thể đăng nhập lúc này'})

#         # Log incoming request data for debugging
#         print("GoogleView_request_data: ", request.data)

#         # Fetch token and email from request
#         token_google = request.data.get("token_google")
#         email = request.data.get("email")
#         print("GoogleView_token_google: ", token_google)
#         print("GoogleView_email: ", email)

#         # Validate the Google token using the /userinfo endpoint
#         payload = {'access_token': token_google}
#         r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)

#         try:
#             data = r.json()  # Parse the Google API response
#         except json.JSONDecodeError as e:
#             print("Error decoding JSON from Google:", str(e))
#             return Response({'message': 'Error decoding Google response'})

#         if 'error' in data:
#             return Response({'message': 'Invalid or expired Google token.'})

#         # Log the Google response data for debugging
#         print("GoogleView_data_from_Google: ", data)

#         # Extract email from the Google API response
#         email = data.get("email")
#         print("GoogleView_email_from_Google: ", email)

#         # Check if user exists, otherwise create a new user
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             print("GoogleView_User.DoesNotExist, creating new user")
#             first_name = data.get("given_name", "")
#             last_name = data.get("family_name", "")
#             user = User(
#                 username=email,
#                 password=make_password(BaseUserManager().make_random_password()),
#                 email=email,
#                 first_name=first_name,
#                 last_name=last_name
#             )
#             user.save()

#         # Generate JWT tokens for the user
#         token = RefreshToken.for_user(user)
#         response = {
#             'access': str(token.access_token),
#             'refresh': str(token)
#         }
#         return Response(response)
    
# class GoogleAuth(APIView):
# def post(self, request):
#     data = request.data
#     token = data.get('credential')
#     try:
#         idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), google_client_id)

#         if not (idinfo["aud"] == google_client_id == data.get("clientId")):
#             raise ValidationError("Invalid client ID.")
#     except:
#         # Invalid token
#         return Response({"status": "invalid token"}, status=400)
#     else:
#         userid = str(idinfo['sub'])
#         email = idinfo.get('email')
#         name = idinfo.get("name")
#         google_users_group, created = Group.objects.get_or_create(name="google_users")


#         user = google_users_group.user_set.filter(google_id=userid)
#         user_exists = user.exists()
#         if user_exists:# login account
#             user = user.first()
#         else: # create account
#             username = random_username_from_name(name)
#             user = User.objects.create_user(username=username, email=email, name=name, password="",
#                                             groups=[google_users_group], hash=False, google_id=userid)
#             picture_url = idinfo.get("picture", None)
#             if picture_url is not None:
#                 add_image_from_url(user, "avatar", picture_url)
#         return return_user_data(user)
