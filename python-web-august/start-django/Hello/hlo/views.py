from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "basic/home.html")
    # return HttpResponse("This is my home function..")

def contact(request):
    return HttpResponse("this is contact us.")
    # return "tis is ok"

def aboutus(request):
    return HttpResponse("this is bout")