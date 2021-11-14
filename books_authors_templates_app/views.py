from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'books':Book.objects.all(),
        'authors':Author.objects.all()
    }
    return render(request, "index.html", context)

def createBook(request):
    Book.objects.create(title=request.POST['book_title'], desc=request.POST['book_desc'])
    return redirect('/')

def createAuthor(request):
    Author.objects.create(first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], 
        notes=request.POST['notes']
    )
    return redirect('/')

def addAuthor(request):
    return render(request, 'add-author-test.html')

def view_book(request, id):
    context = {
        'book':Book.objects.get(id=id),
        'authors':Author.objects.all()
    }
    return render(request, "view-book.html", context)

def createRel(request, id):
    book = Book.objects.get(id=id)
    authorID = request.POST['authors']
    author=Author.objects.get(id=authorID)
    book.authors.add(author)
    return redirect('/')