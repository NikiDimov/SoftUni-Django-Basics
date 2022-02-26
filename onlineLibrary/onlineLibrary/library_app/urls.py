from django.urls import path

from onlineLibrary.library_app.views import show_index, add_book, edit_book, book_details, profile_page, edit_profile, \
    delete_profile, create_profile, delete_book

urlpatterns = [
    path('', show_index, name='show index'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('details/<int:pk>', book_details, name='book details'),
    path('delete/<int:pk>', delete_book, name='delete book'),

    path('profile/', profile_page, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
