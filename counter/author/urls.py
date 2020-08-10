from author.views import update_count
from django.urls import path

urlpatterns = [
    path('add_book/', update_count)
]
