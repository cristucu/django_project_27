from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

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
        form = BookForm(request.POST)
        if form.is_valid():
            # aici se creaza un book in baza de date!
            form.save()
            return redirect("create_book")
    else:
        # in cazul acesta, request-ul poate fi GET, PUT, PATCH, DELETE...
        form = BookForm()
    return render(request, "books/book_form.html", context={"form": form})

def delete_book(request: HttpRequest, pk: int):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("home")

    return render(request, "books/book_confirm_delete.html", context={"book": book})