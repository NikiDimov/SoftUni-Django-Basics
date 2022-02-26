from django.contrib import admin

from onlineLibrary.library_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

