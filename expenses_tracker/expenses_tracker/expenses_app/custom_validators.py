from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters.")


@deconstructible
class MaxFileSizeInMBValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(f"Max file size is {self.max_size:.2f} MB")

