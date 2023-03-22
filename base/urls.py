#專門給base app 用的 urls
from django.urls import path
from . import views

urlpatterns = [
  path('',views.home, name = "home"),
  path('room/<str:pk>/',views.room , name = "room"),
]
