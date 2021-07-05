from django.contrib import admin
from django.urls import path

from main.views import index, detail, create, delete, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('detail/<int:pk>/', detail),
    path('create/', create),
    path('delete/<int:pk>/', delete),
    path('edit/<int:pk>/', edit),
]
