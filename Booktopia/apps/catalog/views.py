

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import BookForm


def book_list(request):
    """Список книг"""
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})


def book_create(request):
    """Добавить новую книгу"""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:book-list')
    else:
        form = BookForm()
    return render(request, 'catalog/book_form.html', {'form': form, 'title': 'Добавить книгу'})


def book_edit(request, book_id):
    """Редактировать книгу"""
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('catalog:book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'catalog/book_form.html', {'form': form, 'title': 'Редактировать книгу'})


def book_delete(request, book_id):
    """Удалить книгу"""
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('catalog:book-list')
    return render(request, 'catalog/book_confirm_delete.html', {'book': book})


def book_detail(request, book_id):
    """Детальная страница книги"""
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'catalog/book_detail.html', {'book': book})