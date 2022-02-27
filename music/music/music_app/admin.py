from django.contrib import admin

from music.music_app.models import Profile, Album


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    pass
