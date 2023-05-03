from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.BooksView.as_view()),
    path("books/<int:book_id>/", views.BooksDetailView.as_view()),
]
