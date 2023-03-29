from django.shortcuts import render, redirect
from .forms import BookAddForm, CategoryAddForm
from .models import Category, Book

# Create your views here.
def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def category_add(request):
    form = CategoryAddForm()
    context = {"form": form}

    if request.method == "POST":
        catgry = Category()
        catgry.category_name = request.POST.get('category_name')
        catgry.save()

    return render(request, 'categories/category_add.html', context)


def book_add(request):
    add_book = BookAddForm()
    category = Category.objects.all()
    context = {"form": add_book, "category": category}

    if request.method == "POST":
        category = Category.objects.get(id=request.POST.get('category'))

        book = Book()
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.category = category
        book.save()
        return redirect('list-book')
    return render(request, 'books/book_add.html', context)


def book_index(request):
    books = Book.objects.all()
    context = {"data": books}
    return render(request, 'books/book_index.html', context)

def category_index(request):
    category = Category.objects.all()
    context = {"data": category}
    return render(request, 'categories/category_index.html', context)