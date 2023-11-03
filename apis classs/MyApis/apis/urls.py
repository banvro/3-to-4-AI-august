from django.urls import path
from apis import views

urlpatterns = [
    path("first-api", views.myfirstapi),
    path("save-data", views.saveinfo)
]