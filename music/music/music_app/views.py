from django.shortcuts import render, redirect

from music.music_app.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from music.music_app.models import Profile, Album


def get_profile():
    user = Profile.objects.all()
    if user:
        return user[0]


def show_index(request):
    user = get_profile()
    albums = Album.objects.all()
    if not user:
        return redirect('create profile')
    context = {
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
        context = {'form': form}
        return render(request, 'add-album.html', context)
    else:
        form = AddAlbumForm()
        context = {'form': form}
        return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {'album': album}
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)
        context = {'form': form, 'album': album}
        return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)
        context = {'form': form, 'album': album}
        return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
        context = {
            'no_profile': True,
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)
    else:
        form = CreateProfileForm()
        context = {
            'no_profile': True,
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)


def profile_details(request):
    albums_count = Album.objects.count()
    context = {'user': get_profile(), 'albums_count': albums_count}
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=get_profile())
        albums = Album.objects.all()
        if form.is_valid():
            form.save()
            albums.delete()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=get_profile())
        context = {'form': form}
        return render(request, 'profile-delete.html', context)
