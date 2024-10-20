from django.contrib.auth.models import User, Group, Permission
from django.core.validators import EmailValidator
# from django.db.models import fields
# from django.utils.crypto import get_random_string
# from requests.api import request
from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
# from django.core.mail import send_mail, EmailMessage
# from django.template.loader import render_to_string
# from django.conf import settings
import socket
import calendar
import time
from getmac import get_mac_address as gma
# from user_agents import parse
# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.hashers import make_password
# from datetime import timedelta, datetime

from api.models import *


def _token_get_exp(access_token):
    try:
        access_token = AccessToken(access_token)
        return access_token["exp"]
    except Exception as error:
        print("===_token_get_exp", error)
        return None

class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "phone"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            # "email":{"validators"+[EmailValidator]},
        }

    def is_email_exist(self):
        try:
            user = User.objects.get(email=self.validated_data["email"])
            return True
        except:
            return False
        
    def save(self):
        user = User(
            email = self.validated_data["email"],
            username = self.validated_data["email"],
            first_name = self.validated_data["first_name"],
            last_name = self.validated_data["last_name"]
        )
        password = self.validated_data["password"]

        user.set_password(password)
        user.is_active = False
        user.save()

        return user
    
class MySimpleJWTSerializer(TokenObtainPairSerializer):
    my_ip_address = "0.0.0.0"
    myRequest = None


    @classmethod
    def get_token(cls, user):
        # print("user: ", user)
        token = super().get_token(user)
        user_obj = User.objects.get(username=user)
        #
        token["email"] = user_obj.email


        access_token = str(token.access_token)
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        mac_address = gma()
        sessionToken = SessionToken.objects.filter(user=user).count()
        if sessionToken == 0:
            sessionToken = SessionToken.objects.get_or_create(
                user=user,
                token=access_token,
                hostname=hostname,
                ip_address=MySimpleJWTSerializer.my_ip_address,
                mac_address=mac_address,
            )
        else:
            sessionToken = SessionToken.objects.get(user=user)
            token_temp = sessionToken.token
            mac_address_temp = sessionToken.mac_address
            ip_address_temp = sessionToken.ip_address


            #
            exp = _token_get_exp(token_temp)
            if exp is not None:
                ts_now = calendar.timegm(time.gmtime())
                if ts_now < exp:
                    pass
            else:
                SessionToken.objects.filter(user=user).update(
                    token=access_token,
                    hostname=hostname,
                    ip_address=MySimpleJWTSerializer.my_ip_address,
                    mac_address=mac_address,
                )
                print(token)
        return token







class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MySimpleJWTSerializer

