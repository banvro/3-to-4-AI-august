from rest_framework import serializers
from apis.models import helobase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class mydataserlizer(serializers.ModelSerializer):
    class Meta: 
        model = helobase
        fields = '__all__'
        # fields = ["id", "title"]

class Userserlizer(serializers.ModelSerializer):
    class Meta: 
        model = User
        # fields = '__all__'
        fields = ["id", "username", "email", "first_name", "last_name"]

        def validate_password(self, value: str) -> str:
            return make_password(value)
