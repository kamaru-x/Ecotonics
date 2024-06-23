from django.urls import path
from Frontend import views

urlpatterns = [
    path('',views.index,name='index'),
]