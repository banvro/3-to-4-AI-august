from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from hlo.models import ContactU

# Create your views here.
def home(request):
    return render(request, "basic/home.html")
    return HttpResponse("This is my home function..")

def contact(request):
    return render(request,"auth/contact.html")
    
def aboutus(request):
    return render(request,"basic/about.html")

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


def loginpage(request):
    if request.method == "POST":
        x = request.POST.get("username")
        y = request.POST.get("password")

        check = authenticate(username = x, password = y)

        if check is not None:
            login(request, check)

    return render(request, "auth/login.html")


def logoutthis(request):
    logout(request)
    return redirect("login")


def contact(request):
     if request.method == "POST":
         Email = request.POST.get("Email")
         password = request.POST.get("Password")

         
        
def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("email")
        msg = request.POST.get("msg")

        sav = ContactU(Name = name, phone_number = number, Email = email, message = msg)
        sav.save()
        
        return redirect("showdata")

    return render(request, "basic/contact.html")



def showdata(request):
    data = ContactU.objects.all()
    return render(request, "basic/showdata.html", {"mydata" : data})



def updatedata(request, x):
    data = ContactU.objects.get(id = x)
    return render(request, "basic/updatedata.html", {"mydata" : data})


def updatenow(request, x):
    x = ContactU.objects.get(id = x)
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("email")
        msg = request.POST.get("msg")

        x.Name = name
        x.Email = email
        x.phone_number = number
        x.message = msg 
        x.save()
        
        return redirect("showdata")
    
    return render(request, "basic/updatedata.html")

def detethis(request, x):
    x = ContactU.objects.get(id = x)
    x.delete()
    return redirect("showdata")