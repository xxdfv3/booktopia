from django.urls import path
from . import views

app_name = 'catalog'  # Важно для namespaces!

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('book/<int:book_id>/', views.book_detail, name='book-detail'),
    path('book/add/', views.book_create, name='book-create'),
    path('book/<int:book_id>/edit/', views.book_edit, name='book-edit'),
    path('book/<int:book_id>/delete/', views.book_delete, name='book-delete'),
]