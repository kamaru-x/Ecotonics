from django.urls import path
from Technicians import views

urlpatterns = [
    path('technicians/',views.technicians,name='technicians'),
    path('technician/add/',views.add_technician,name='add-technician'),
    path('technician/delete/<int:technician_id>',views.delete_technician,name='delete-technician'),
]