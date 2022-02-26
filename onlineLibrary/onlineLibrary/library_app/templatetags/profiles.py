from django import template

from onlineLibrary.library_app.models import Profile

register = template.Library()


@register.simple_tag()
def profile_name():
    users = Profile.objects.all()
    if users:
        return users[0].first_name
