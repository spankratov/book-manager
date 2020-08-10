from django.urls import path

from author.views import update_count

urlpatterns = [
    path('add_book/', update_count)
]
