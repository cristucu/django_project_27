from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book


# Create your views here.

# functions that manage our web pages

def home(request: HttpRequest):
    return HttpResponse("Hello from our books app!")

# function-based view:
# CRUD: Create, Read, Update, Delete
def list_books(request: HttpRequest):
    # trebuie sa listam cartile din baza de date
    # accesare de carti:
    books = Book.objects.all()
    return render(request, "books/home.html", context={"books": books})

def create_book(request: HttpRequest):
    if request.method == "POST":
        # detaliile book-ului care au fost trimise de form folosind HTTP POST request, se afla in request.POST ca un dictionar.
        book_instance = BookForm(request.POST)
        if book_instance.is_valid():
            # aici se creaza un book in baza de date!
            book_instance.save()
            return redirect("create_book")
    else:
        # in cazul acesta, request-ul poate fi GET, PUT, PATCH, DELETE...
        form = BookForm()
        list1 = [10, 20, 30, 40]
        return render(request, "books/book_form.html", context={"form": form, "list1":list1}

                  )
