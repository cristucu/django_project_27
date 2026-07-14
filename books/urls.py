from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_books, name="home"),
    path("create_book/", views.create_book, name="create_book")
]