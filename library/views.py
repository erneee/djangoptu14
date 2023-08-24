from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Book, Author, BookInstance, Genre


def index(request):
    numb_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact='g').count()
    numb_of_authors = Author.objects.all().count()

    context_t = {
        'numb_books_t': numb_books,
        'num_instance_t': num_instance,
        'num_instance_available_t': num_instance_available,
        'numb_of_authors_t': numb_of_authors,
    }

    return render(request, 'index.html', context=context_t)

def authors(request):
    authors = Author.objects.all()
    print(authors)
    context_t = {
        'author_t': authors,

    }
    return render(request, 'authors.html', context_t)


def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    context_t = {
        'author_t': single_author,
    }

    return render(request, 'author.html', context_t)


class BookListView(generic.ListView):
    model = Book #modelioklase_list -> book_list
    template_name = 'book_list.html'


