from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:name>", views.sapa, name='sapa'),
    path("al", views.al, name='al'),
    path('abi', views.abi, name='abi')
]
