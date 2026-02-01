from django.urls import path
from .views import index, dashboard, create_category, delete_fruit, details_fruit, edit_fruit, create_fruit


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create-fruit/', create_fruit, name='create-fruit'),
    path('details/<int:pk>/', details_fruit, name='details-fruit'),
    path('edit/<int:pk>/', edit_fruit, name='edit-fruit'),
    path('delete/<int:pk>/', delete_fruit, name='delete-fruit'),
    path('create-category/', create_category, name='create-category'),
]