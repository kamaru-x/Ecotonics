from django.urls import path
from Works import views

urlpatterns = [
    path('work/service/calls/',views.service_calls,name='service-calls'),
    path('work/service/call/add/',views.add_service_call,name='add-service-call'),
]