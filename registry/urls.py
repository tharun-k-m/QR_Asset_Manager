from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Changed from dashboard to home
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'), # Move dashboard to its own path
    path('items/new/', views.create_item, name='create_item'),
    path('items/<uuid:pk>/', views.item_detail, name='item_detail'),
    path('items/<uuid:pk>/edit/', views.edit_item, name='edit_item'),
    path('items/<uuid:pk>/delete/', views.delete_item, name='delete_item'),
]