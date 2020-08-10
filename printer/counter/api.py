from django.conf import settings
import requests


class CounterApi:
    url = settings.COUNTER_URL

    @classmethod
    def add_book(cls, author_name: str) -> bool:
        r = requests.post(f'{cls.url}/author/add_book/', json={'author_name': author_name})
        return r.status_code == requests.codes.ok
