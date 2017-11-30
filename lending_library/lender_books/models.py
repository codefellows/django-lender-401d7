from django.db import models
import datetime


class Book(models.Model):
    cover_image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(null=True)

    YEARS = [(year, year)
         for year in range(1, datetime.datetime.now().year + 1)][::-1]
    year = models.IntegerField(choices=YEARS, default=2016)

    BOOK_STATUS = [
        ("available", "Available"),
        ("checked out", "Checked Out")
    ]
    status = models.CharField(
        max_length=20,
        choices=BOOK_STATUS,
        default="available"
    )
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)
