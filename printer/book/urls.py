from book.views import CreateBookView
from django.urls import path

urlpatterns = [
    path('add_book/', CreateBookView.as_view())
]
