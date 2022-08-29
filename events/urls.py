from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("month_form", views.month_form, name="month_form"),
    path("search_form", views.search_form, name="search_form"),

    path("tag/<str:tag_name>", views.tag, name="tag"),

    path("tag_days/<int:days>/<str:tag_name>", views.tag_days, name="tag_days"),
    path("search_words/<int:days>/<str:words>", views.search_words, name="search_words"),
    path("stars_between/<int:days>/<int:lower_bound>/<int:upper_bound>", views.stars_between, name="stars_between"),

    path("month/<int:year>/<int:month>", views.month, name="month"),
    path("<int:days_back>", views.index, name="index_days_back"),
]
