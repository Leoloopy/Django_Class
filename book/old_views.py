from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Publisher
from .models import Book
from .forms import BookForm


# from django.db.models import

# Create your views here.

def index(request):
    # queryset = Publisher.objects.filter(name="Jaxspan")
    # queryset = Publisher.objects.filter(website__startswith="https")
    # queryset = Publisher.objects.filter(id__in=(1, 2, 3))
    # queryset = Publisher.objects.filter(id__range=(5, 8))
    queryset = Publisher.objects.all()
    return render(request, "publisher-index.html", context={"publishers": list(queryset)})


def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, "publisher-details.html", context={"publisher": publisher})


def book_index(request):
    queryset = Book.objects.order_by("title")
    return render(request, "book-index.html", context={"book": list(queryset)})


def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book-details.html", context={"book": book})


def book_create(request):
    form = BookForm()

    if request.method == 'POST':
        print(request.POST)
        form = BookForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return render(request, 'book/book-create.html', context={"form": form})

    else:
        return render(request, 'book/book-create.html', context={"form": form})


