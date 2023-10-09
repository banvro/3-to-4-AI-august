from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, "basic/home.html")
    # return HttpResponse("This is my home function..")

def contact(request):
    return HttpResponse("this is contact us.")
    # return "tis is ok"

def aboutus(request):
    return HttpResponse("this is bout")

def signup(request):
    return render(request, "auth/signup.html")


def savedata(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        userinfo = User.objects.create_user(username = uname, first_name = firstname, last_name = lastname, email = email, password = password)
        userinfo.save()
        return redirect("signup")
    return HttpResponse("data saved")