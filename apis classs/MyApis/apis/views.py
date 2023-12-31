from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apis.models import helobase
from apis.serializer import Userserlizer, mydataserlizer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(["GET"])
def myfirstapi(request):
    data = helobase.objects.all().order_by("-id")
    serlizer = mydataserlizer(data, many = True)
    return Response({"mesage" : "This is my first api",
                     "Data" : serlizer.data})

@api_view(["POST"])
def saveinfo(request):
    xyz = mydataserlizer(data = request.data)
    if xyz.is_valid():
        xyz.save()

    return Response({
        "message" : "Data Save sucessfully",
        "data" : xyz.data
    })

@api_view(["POST"])
def createnewuser(request):
    xyz = Userserlizer(data = request.data)
    if xyz.is_valid():
        xyz.is_valid(raise_exception=True)
        user = xyz.save(is_active=True)
        token = get_tokens_for_user(user)
        
    return Response({
        "message" : "User Added sucessfully",
        "data" : xyz.data,
        "tokens" : token
    })




@api_view(["PATCH"])
def updatethis(request, x):
    obj = helobase.objects.get(id = x)
    xyz = mydataserlizer(obj, data = request.data, partial = True)
    if xyz.is_valid():
        xyz.save()

    return Response({
        "message" : "data Updateed sucessfully",
        "data" : xyz.data
    })

@api_view(["POST"])
def deletethis(request, x):
    obj = helobase.objects.get(id = x)
    obj.delete()

    return Response({
        "message" : "data Deleted sucessfully"
    })