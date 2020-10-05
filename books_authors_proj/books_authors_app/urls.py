from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('books/create', views.addBook),
    path("authors", views.authors),
    path("authors/create", views.addAuthor),
    path("books/<int:book_id>", views.bookProfile),
    path("authors/<int:author_id>", views.authorProfile)
    
]