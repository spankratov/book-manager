import random

from locust import HttpUser, between, task


class QuickstartUser(HttpUser):
    wait_time = between(5, 9)
    authors = ['Leo Tolstoy', 'Fyodor Dostoevsky']
    books = [
        'War and Peace',
        'Crime and Punishment',
        'War and Punishment',
        'Crime and Peace',
    ]

    @task
    def print_book(self):
        author = random.choice(self.authors)
        book = random.choice(self.books)
        self.client.post(
            "/book/add_book/",
            json={"title": book, "author": author},
        )
