import re

from django.core.exceptions import ValidationError


def validate_only_letters_nums(value):
    if not re.match("^[A-Za-z0-9_]*$", value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

