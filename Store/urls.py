from django.urls import path
from . import views

app_name = 'Store'

urlpatterns = [
    path('', views.store, name='store'),
]