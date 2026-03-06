from django.urls import path
from . import views

app_name = 'catalog'  # Важно для namespaces!

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('book/<int:book_id>/', views.book_detail, name='book-detail'),
]