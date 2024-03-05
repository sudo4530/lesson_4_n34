from django.urls import path
from .views import landingView, books_view

urlpatterns =[
    path("", landingView, name='landing'),
    path("books/", books_view, name='books'),
]