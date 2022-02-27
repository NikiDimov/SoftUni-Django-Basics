from django.core.validators import MinLengthValidator, MinValueValidator, EmailValidator
from django.db import models

from music.music_app.custom_validators import validate_only_letters_nums


class Profile(models.Model):
    USER_NAME_MIN_LEN = 2
    USER_NAME_MAX_LEN = 15
    AGE_MIN_VALUE = 0

    username = models.CharField(max_length=USER_NAME_MAX_LEN,
                                validators=[MinLengthValidator(USER_NAME_MIN_LEN), validate_only_letters_nums])
    email = models.EmailField(validators=[EmailValidator])
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(AGE_MIN_VALUE)])


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    PRICE_MIN_VALUE = 0.0
    GENRE_CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )
    album_name = models.CharField(max_length=ALBUM_NAME_MAX_LEN, unique=True)
    artist = models.CharField(max_length=ARTIST_MAX_LEN)
    genre = models.CharField(
        max_length=max([len(x) for x, _ in GENRE_CHOICES]),
        choices=GENRE_CHOICES)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(PRICE_MIN_VALUE)])

    def save(self, *args, **kwargs):
        self.price = round(self.price, 2)
        super(Album, self).save(*args, **kwargs)
