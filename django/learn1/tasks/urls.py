from django.urls import path
from . import views

app_name = "tasks"
# untuk menghindari collision, kita beri app_name variable untuk membuat dia menjadi unik
urlpatterns = [
    path("", views.index, name='index'),
    path("add", views.add, name='add') 
]