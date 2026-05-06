from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('add', views.add, name='result.html')
]
