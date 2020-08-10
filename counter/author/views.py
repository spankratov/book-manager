import json

from django.db.models import F
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from author.models import Author


@require_POST
@csrf_exempt
def update_count(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    if 'author_name' not in data:
        return HttpResponseBadRequest('author_name field is required')

    author_name = str(data['author_name'])
    updated = Author.objects.filter(name=author_name).update(books_count=F('books_count')+1)
    if not updated:
        Author.objects.create(
            name=author_name,
            books_count=1,
        )
    return HttpResponse('OK')
