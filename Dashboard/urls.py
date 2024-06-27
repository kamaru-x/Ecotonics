from django.urls import path
from Dashboard import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    path('sites/',views.sites,name='sites'),
    path('site/create/',views.create_site,name='create-site'),

    path('cash/categories/',views.categories,name='categories'),
    path('cash/category/add/',views.add_category,name='add-category'),
    path('cash/category/delete/<int:cid>/',views.delete_category,name='delete-category'),

    path('cash/transactions/',views.transactions,name='transactions'),
    path('cash/transaction/add/',views.add_transaction,name='add-transaction'),
    path('cash/transaction/delete/<int:tid>/',views.delete_transaction,name='delete-transaction'),
]