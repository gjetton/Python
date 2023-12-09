# urls.py

from django.urls import path
from .views import item_list, add_item, edit_item

urlpatterns = [
    path('items/', item_list, name='item_list'),
    path('items/add/', add_item, name='add_item'),
    path('items/<int:item_id>/edit/', edit_item, name='edit_item'),
]
