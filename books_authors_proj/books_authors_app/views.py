from django.shortcuts import render
from books_authors_app.models import *
# Create your views here.
def index(request):
    context ={
        'allBooks': Book.objects.all()
    }
    return render(request, 'index.html', context)

def addBook(request):
    pass

def bookProfile(request, book_id):
    context = {
        'requested_book':Book.objects.get(id=str(book_id))
    }
    return render(request, 'book_profiles.html', context)

def authors(request):
    context ={
        'allAuthors': Author.objects.all()
    }
    return render(request, 'author.html', context)

def addAuthor(request):
    pass
def authorProfile(request, author_id):
    context = {
        'requested_author':Author.objects.get(id=str(author_id))
    }
    return render(request, 'author_profiles.html', context)
