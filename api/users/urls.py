from django.urls import path
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path("", views.get_user_list),
    path("sign_in", auth_views.obtain_auth_token),
    path("sign_up", views.sign_up),
]
