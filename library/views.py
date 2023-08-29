from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from django.db.models import Q
from django.core.paginator import Paginator


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
    paginator = Paginator(Author.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)
    print(authors)
    context_t = {
        'author_t': paged_authors,

    }
    return render(request, 'authors.html', context_t)


def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    context_t = {
        'author_t': single_author,
    }

    return render(request, 'author.html', context_t)


class BookListView(generic.ListView):# grazins visas eilutes is lenteles
    model = Book #modelioklase_list -> book_list
    # context_object_name = 'my_book_list' turetume template pakeisti for loopa
    template_name = 'book_list.html'
    paginate_by = 3 # sukuria page_obj darbui su puslapiais

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'



def search(request):
    query = request.GET.get('search_text')
    search_results = Book.objects.filter(
        Q(title__icontains=query) |
        Q(summary__icontains=query)
    )
    context_t = {
        'query_t': query,
        'search_results_t': search_results,
    }

    return  render(request, 'search.html', context_t)


