from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/<int:pk>/edit/', TaskEditView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/confirm/', DeleteView.as_view(), name='task-delete'),
]