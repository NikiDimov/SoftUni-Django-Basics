from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('The name should consist of only letters!')


def validate_file_max_size(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')
