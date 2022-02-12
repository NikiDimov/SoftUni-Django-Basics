from django.urls import path

from petstagram.main_app.views import show_home, show_dashboard, show_profile, show_pet_photo_details, like_pet_photo, \
    create_profile, add_pet, add_photo, edit_photo, edit_pet, delete_pet, edit_profile, delete_profile

urlpatterns = [
    path('', show_home, name='home'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>', show_pet_photo_details, name='photo details'),
    path('photo/like/<int:pk>', like_pet_photo, name='like pet photo'),

    path('profile/create/', create_profile, name='create profile'),
    path('pet/add/', add_pet, name='add pet'),
    path('pet/edit/<int:pk>', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>', delete_pet, name='delete pet'),
    path('photo/add/', add_photo, name='add photo'),
    path('photo/edit/<int:pk>', edit_photo, name='edit photo'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

]
