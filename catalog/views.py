from catalog.models import Author, Book
from django.shortcuts import redirect, render
from catalog.forms import ModelBookForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
# Create your views here.

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class AuthorsList(ListView):
    model = Author

def update_book(request, pk):
    if request.method == 'POST':
        
        data = request.POST
        author = Author.objects.get(pk=data['author'])
        book = Book.objects.get(pk=pk)
        book.title = data['title']
        book.author = author
        book.editorial = data['editorial']
        book.year = data['year']
        book.volume = data['volume']
        book.save()
        return redirect('/catalog')
    else:
        book = Book.objects.get(pk=pk)
        form = ModelBookForm(book.__dict__)
        return render(request, 'catalog/new.html', {"form": form})


def new_book(request):
    if request.method == 'POST':
        data = request.POST
        book = Book()
        book.title = data['title']
        # book.autor = data['autor']
        book.editorial = data['editorial']
        book.year = data['year']
        book.volume = data['volume']
        book.save()

        return redirect('/catalog')
    else:
        form = ModelBookForm()
        return render(request, 'catalog/new.html', {"form": form})

def get_books_by_editorial(request, editorial):
    books = Book.objects.filter(editorial = editorial)
    year = request.GET.get("year")
    if year != None:
        books = books.filter(year=year)

    return render(request, 'catalog/index.html', {'books': books})
def catalog_list(request):
    books = Book.objects.all()
    # books = Book.objects.filter(editorial = "Conecta")
    # gt = mayor, lt = menor, gte = mayor que, lte = menor que
    # books = Book.objects.filter(year__gte = 2018)
    # contains= contiene
    # books = Book.objects.filter(title__contains = "MBA")

    return render(request, 'catalog/index.html', {'books': books})
