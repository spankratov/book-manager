from book.serializers import BookSerializer
from book.tasks import send_to_counter
from rest_framework import generics


class CreateBookView(generics.CreateAPIView):
    serializer_class = BookSerializer

    def perform_create(self, serializer: BookSerializer) -> None:
        book = serializer.save()
        send_to_counter.delay(book.author, book.id)
