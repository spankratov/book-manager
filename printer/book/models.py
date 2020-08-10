from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024)


class CounterErrorLog(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
