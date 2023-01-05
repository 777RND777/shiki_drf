from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_user_detail),
    path("list/anime", views.get_review_list),
]
