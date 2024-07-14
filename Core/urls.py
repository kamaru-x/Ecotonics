from django.urls import path
from Core import views

urlpatterns = [
    path('services/',views.services,name='services'),
    path('service/add/',views.add_service,name='add-service'),
    path('service/delete/<int:service_id>/',views.delete_service,name='delete-service'),
]