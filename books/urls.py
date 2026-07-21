from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_books, name="home"),
    path("create_book/", views.create_book, name="create_book"),
    path("delete_book/<int:pk>/", views.delete_book, name="delete_book"),
    path("update_book/<int:pk>/", views.update_book, name='update_book')]