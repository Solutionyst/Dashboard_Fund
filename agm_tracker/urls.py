from django.urls import path
from agm_tracker import views

urlpatterns = [

    path('agm-tracker/', views.agm_tracker, name='agm_tracker'),
    path('new-agm/', views.new_agm, name='new_agm'),
    path('agm_delete/<str:pk>', views.agm_delete, name='delete_agm'),
]