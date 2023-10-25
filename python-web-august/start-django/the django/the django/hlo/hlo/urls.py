from django.urls import path
from hlo import views
urlpatterns = [
    path("", views.home, name = "Home"),
    path("home", views.home, name = "Home"),
    path("Naveen", views.home, name = "Naveen"),
    path("contact", views.contact, name = "contact"),
    path("about", views.aboutus,name= "About"),
    path("contact", views.contact, name = "contact"),
    path("signup", views.signup, name = "signup"),
    path("savedata", views.savedata), 

    path("login-page", views.loginpage, name="login"),
    path("logoutthis", views.logoutthis),

    path("contactus", views.contactus),
    path("showdata", views.showdata, name = "showdata"),

    path("updatedata/<int:x>", views.updatedata, name = "updatedata"),

    path("updatenow/<int:x>", views.updatenow, name = "updatenow"),

    path("delete/<int:x>", views.detethis),

]