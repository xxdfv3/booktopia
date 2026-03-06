

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def book_list(request):
    """Список книг"""
    # Пока заглушка
    books = []
    return render(request, 'catalog/book_list.html', {'books': books})

def book_detail(request, book_id):
    """Детальная страница книги"""
    return HttpResponse(f"Книга ID: {book_id}")