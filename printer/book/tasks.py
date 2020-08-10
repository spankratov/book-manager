from celery import shared_task

from book.models import CounterErrorLog
from counter.api import CounterApi


@shared_task
def send_to_counter(author_name: str, book_id: int):
    status = CounterApi.add_book(author_name)
    if not status:
        CounterErrorLog.objects.create(book_id=book_id)
