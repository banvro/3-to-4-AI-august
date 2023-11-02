from rest_framework import serializers
from apis.models import helobase

class mydataserlizer(serializers.ModelSerializer):
    class Meta: 
        model = helobase
        fields = '__all__'
