from django.shortcuts import render, redirect

from books.book_app.forms import BookForm
from books.book_app.models import Book


def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = BookForm()
        context = {'form': form}
        return render(request, 'create.html', context)
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'form': form}
    return render(request, 'create.html', context)


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "GET":
        form = BookForm(instance=book)
        context = {'form': form}
        return render(request, 'edit.html', context)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        book.save()
        return redirect('index')
    context = {'form': form}
    return render(request, 'edit.html', context)
