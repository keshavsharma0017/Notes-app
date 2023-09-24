from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes),
    path('notes/create/', views.postnotes),
    path('notes/<str:pk>/update/', views.updatenotes),
    path('notes/<str:pk>/delete/', views.deleteNotes),
]
