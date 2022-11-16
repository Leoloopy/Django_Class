from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here

class Book(models.Model):
    GENRE_CHOICES = {
        ("C", "Comedy"),
        ("T", "Tragedy"),
        ("TC", "Tragicomedy"),
        ("CR", "Crime"),
        ("R", "Romance"),
        ("SF", "Science Fiction"),
    }
    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True)
    isbn = models.CharField(max_length=20)
    date_published = models.DateField()
    date_added = models.DateField(auto_now_add=True)
    edition = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default="R")


class Author(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()


class Publisher(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    website = models.URLField()


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=6, validators=[MinLengthValidator(5, "code cannot be less than a length 5"),
                                                         MaxLengthValidator(6, "code cannot exceed a length of 6")])

