from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("month_form", views.month_form, name="month_form"),
    path("tag/<str:tag_name>", views.tag, name="tag"),
    path("month/<int:year>/<int:month>", views.month, name="month"),
    path("<int:days_back>", views.index, name="index_days_back"),
]
