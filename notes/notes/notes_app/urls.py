from django.urls import path

from notes.notes_app.views import show_index, add_note, edit_note, delete_note, note_details, profile_page, \
    create_profile

urlpatterns = [
    path('', show_index, name='show index'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', note_details, name='note details'),
    path('profile/', profile_page, name='profile page'),
    path('profile/create/', create_profile, name='create profile')
]
