from django.urls import path
from apis import views

urlpatterns = [
    path("first-api", views.myfirstapi),
    path("save-data", views.saveinfo),
    path("update-data/<int:x>", views.updatethis),
    path("delete-data/<int:x>", views.deletethis)
]