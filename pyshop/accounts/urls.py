from django.urls import path
from . import views
urlpatterns = [
    path("",views.register),
    path("login/",views.login),
    path("logout/",views.logout)
]