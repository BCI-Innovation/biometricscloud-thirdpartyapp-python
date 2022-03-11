from django.urls import path

from . import views

urlpatterns = [
    path('appauth/code', views.authorize, name='index'),
    path('', views.index, name='index'),
]
