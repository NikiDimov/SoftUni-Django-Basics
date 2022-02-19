from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.expenses_app.custom_validators import validate_only_letters, MaxFileSizeInMBValidator


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 15
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    BUDGET_DEFAULT_VAL = 0
    BUDGET_MIN_VAL = 0
    IMAGE_UPLOAD_TO_DIR = 'profiles/'
    IMAGE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LEN,
                                  validators=[MinLengthValidator(FIRST_NAME_MIN_LEN), validate_only_letters])
    last_name = models.CharField(max_length=LAST_NAME_MAX_LEN,
                                 validators=[MinLengthValidator(LAST_NAME_MIN_LEN), validate_only_letters])

    budget = models.FloatField(default=BUDGET_DEFAULT_VAL, validators=[MinValueValidator(BUDGET_MIN_VAL)])

    profile_image = models.ImageField(upload_to=IMAGE_UPLOAD_TO_DIR, null=True, blank=True,
                                      validators=[MaxFileSizeInMBValidator(IMAGE_MAX_SIZE_IN_MB)])

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(max_length=TITLE_MAX_LEN)
    expense_image = models.URLField(verbose_name='Link to Image')
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
