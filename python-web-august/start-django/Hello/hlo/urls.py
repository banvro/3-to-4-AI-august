from django.urls import path
from hlo import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("contact", views.contact, name = "contact"),
    path("about", views.aboutus),
    path("contact", views.contact, name = "contact"),
    path("signup", views.signup, name = "signup"),
    path("savedata", views.savedata), 

    path("login-page", views.loginpage, name="login"),
    path("logoutthis", views.logoutthis),
]
