from django.urls import path
from app import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='Dashboard'),
]