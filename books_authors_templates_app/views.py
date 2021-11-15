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
    return redirect('/addAuthor')

def addAuthor(request):
    context = {
        'authors':Author.objects.all()
    }
    return render(request, 'index-auth.html', context)

def view_book(request, id):
    context = {
        'book':Book.objects.get(id=id),
        'authors':Author.objects.all()
    }
    return render(request, "view-book.html", context)

def view_author(request, id):
    print(request.build_absolute_uri())
    context = {
        'books':Book.objects.all(),
        'author':Author.objects.get(id=id)
    }
    return render(request, "view-author.html", context)


def createRel(request, id):
    test_pg = request.build_absolute_uri()
    if "author" in test_pg:
        book = Book.objects.get(id=id)
        authorID = request.POST['authors']
        author=Author.objects.get(id=authorID)
        book.authors.add(author)
        return redirect(f'/view-book/{id}')
    else:
        author = Author.objects.get(id=id)
        bookID = request.POST['books']
        book=Book.objects.get(id=bookID)
        author.books.add(book)
        return redirect(f'/view-author/{id}')