from django.urls import path

from book.views import CreateBookView

urlpatterns = [
    path('add_book/', CreateBookView.as_view())
]
