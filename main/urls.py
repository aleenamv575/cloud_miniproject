from django.urls import path
from . import views
urlpatterns  = [
    path('', views.index),
    path('track',views.home),
    path('get_data', views.getData)
]