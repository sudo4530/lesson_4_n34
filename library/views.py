from django.shortcuts import render
from .models import Book, Student, Booking

def landingView(request):
    return render(request, "library/landing_page.html")


def books_view(request):
    books = Book.objects.all()
    return render(request, "library/books_list.html", {"books": books})


