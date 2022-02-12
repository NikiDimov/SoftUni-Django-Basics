import datetime

from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models

from petstagram.main_app.custom_validators import only_letters_validator, validate_file_max_size


class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    )
    first_name = models.CharField(
        verbose_name="First Name:",
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )
    last_name = models.CharField(
        verbose_name="Last Name:",
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )
    profile_picture = models.URLField(
        verbose_name="Link to Profile Picture:"
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        validators=(EmailValidator,),
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=max([len(x) for x, _ in GENDER_CHOICES]),
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f" id:{self.id}- {self.first_name}"


class Pet(models.Model):
    TYPE_CHOICES = (
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Bunny", "Bunny"),
        ("Parrot", "Parrot"),
        ("Fish", "Fish"),
        ("Other", "Other"),
    )
    name = models.CharField(max_length=30, verbose_name='Pet Name')
    type = models.CharField(
        max_length=max([len(x) for x, _ in TYPE_CHOICES]),
        choices=TYPE_CHOICES,
    )
    date_of_birth = models.DateField(
        verbose_name='Day of Birth',
        null=True,
        blank=True,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_profile', 'name')

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    photo = models.ImageField(validators=[validate_file_max_size], verbose_name='Pet Image:', upload_to='static/media')
    tagged_pets = models.ManyToManyField(Pet, verbose_name='Tag Pets:')
    description = models.TextField(
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )
