from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:days_back>", views.index, name="index_days_back"),
    path("add", views.add, name="add"),
]
