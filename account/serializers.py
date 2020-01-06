from rest_framework import serializers
from utils.sms import SMS
from .models import *
from django.contrib.auth import authenticate
from .models import *
from djoser.serializers import TokenSerializer


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'userpic', 'email', 'is_active')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'gender', 'user_type', 'phone',
                  'first_name', 'last_name', 'birth_day', 'userpic', 'is_active')


class LoginTokenSerializer(TokenSerializer):
    user = UserSerializer()

    class Meta(TokenSerializer.Meta):
        fields = ('auth_token', 'user')
