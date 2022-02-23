from django.contrib import admin

from notes.notes_app.models import Profile


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass

