from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index,name="list"),
    path('updatetask/<str:pk>/', views.updatetask,name="updatetask"),
    path('deletetask/<str:pk>/', views.deletetask,name="deletetask"),
]
