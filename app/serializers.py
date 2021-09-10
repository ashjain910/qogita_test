from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from rest_framework.fields import CurrentUserDefault


from .models import *
from .constants import *
from datetime import datetime

from django.contrib.auth.models import User

import pytz

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        name = 'user'
        fields = ('first_name', 'last_name', 'email','id')

class AddressSerializer(ModelSerializer):
    #user = UserSerializer(allow_null=True)
    class Meta:
        model = Address
        name = 'address'
        fields = '__all__'
        depth = 1

class AddressReadSerializer(ModelSerializer):
    user = UserSerializer(allow_null=True)
    class Meta:
        model = Address
        name = 'address'
        fields = '__all__'
