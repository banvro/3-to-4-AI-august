from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apis.models import helobase
from apis.serializer import mydataserlizer

# Create your views here.

@api_view(["GET"])
def myfirstapi(request):
    data = helobase.objects.all().order_by("-id")
    serlizer = mydataserlizer(data, many = True)
    return Response({"mesage" : "This is my first api",
                     "Data" : serlizer.data})