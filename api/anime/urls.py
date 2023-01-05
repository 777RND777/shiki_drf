from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_anime_list),
    path("<slug:slug>", views.get_anime_detail),
    path("<slug:slug>/review", views.review_anime),
]
