from django.urls import path
from app import views
from .models import position

urlpatterns = [

    path('', views.index, name='Dashboard'),
    path('new-position/', views.new_position, name='new_position'),
    path('position_delete/<str:pk>', views.Position_Delete, name='Delete_Position'),
]