from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=1024,
        unique=True,
    )
    books_count = models.PositiveIntegerField(default=1)
