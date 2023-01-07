from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_anime_list),
    path('kind/<str:kind>', views.get_anime_list),
    path('status/<str:status>', views.get_anime_list),
    path('genre/<str:genre>', views.get_anime_list),
    path('studio/<str:studio>', views.get_anime_list),
    path('<slug:slug>', views.get_anime_detail),
    path('<slug:slug>/review', views.review_anime),
]
