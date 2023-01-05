from django.urls import path
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path("users", views.get_user_list),
    path("users/sign_in", auth_views.obtain_auth_token),
    path("users/sign_up", views.sign_up),

    path("<slug:slug>", views.get_user_detail),
]
