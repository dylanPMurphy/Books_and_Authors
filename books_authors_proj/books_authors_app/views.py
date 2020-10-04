from django.shortcuts import render
from books_authors_app.models import *
# Create your views here.
def index(request):
    context ={
        'allBooks': Books.objects.all()
    }
    return render(request, index.html, context)