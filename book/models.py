from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify
from django.urls import reverse


# Create your models here

class Publisher(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("publisher-details", args=[self.id])


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
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    authors = models.ManyToManyField("Author", related_name="books")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} ({self.price})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-details", kwargs={"slug": self.slug})


class Author(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=6, validators=[MinLengthValidator(5, "code cannot be less than a length 5"),
                                                         MaxLengthValidator(6, "code cannot exceed a length of 6")])
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE, primary_key=True)
