from django.shortcuts import render, redirect

from notes.notes_app.forms import AddNoteForm, EditNoteForm, CreateProfileForm, DeleteNoteForm
from notes.notes_app.models import Profile, Note


def get_profile():
    user = Profile.objects.all()
    if user:
        return user[0]


def show_index(request):
    user = get_profile()
    if not user:
        return redirect('create profile')
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = AddNoteForm()
        context = {'form': form}
        return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditNoteForm(instance=note)
        context = {'form': form, 'note': note}
        return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteNoteForm(instance=note)
        context = {'form': form, 'note': note}
        return render(request, 'note-delete.html', context)


def note_details(request, pk):
    pass


def profile_page(request):
    pass


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
        context = {
            'form': form,
            'no_profile': True,
        }
        return render(request, 'home-no-profile.html', context)
