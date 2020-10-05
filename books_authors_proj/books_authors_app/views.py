from django.shortcuts import render, redirect
from books_authors_app.models import *
# Create your views here.
def index(request):
    context ={
        'allBooks': Book.objects.all()
    }
    return render(request, 'index.html', context)

def addBook(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')

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
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')
def authorProfile(request, author_id):
    context = {
        'requested_author':Author.objects.get(id=str(author_id))
    }
    return render(request, 'author_profiles.html', context)
