from django.shortcuts import render, redirect

from onlineLibrary.library_app.forms import CreateProfileForm, AddBookForm, DeleteBookForm, EditBookForm, \
    EditProfileForm, DeleteProfileForm
from onlineLibrary.library_app.models import Profile, Book


def get_profile():
    user = Profile.objects.all()
    if user:
        return user[0]


def show_index(request):
    user = get_profile()
    books = Book.objects.all()
    if not user:
        return redirect('create profile')
    context = {
        'user': user,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = AddBookForm()
        context = {'form': form}
        return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditBookForm(instance=book)
        context = {'form': form, 'book': book}
        return render(request, 'edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteBookForm(instance=book)
        context = {'form': form, 'book': book}
        return render(request, 'delete-book.html', context)


def profile_page(request):
    context = {'user': get_profile()}
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
        context = {
            'no_profile': True,
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=get_profile())
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = EditProfileForm(instance=get_profile())
        context = {'form': form}
        return render(request, 'edit-profile.html', context)


def delete_profile(request):
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=get_profile())
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=get_profile())
        context = {'form': form}
        return render(request, 'delete-profile.html', context)
