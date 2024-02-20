from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

from .models import *  # noqa: F403

# from .models import Book, Category

from .forms import BookForm, CategoryForm


def library(request):
    return render(request, "pages/index.html")


def index(request):
    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        # Add
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    # كل المنتجات
    AllItems = {
        "items": Book.objects.all(),  # noqa: F405
        "category": Category.objects.all(),  # noqa: F405
        "form": BookForm(),
        "formCategory": CategoryForm(),
    }
    return render(request, "pages/index.html", AllItems)


def books(request):
    AllItems = {
        "items": Book.objects.all(),  # noqa: F405
        "category": Category.objects.all(),  # noqa: F405
    }
    return render(request, "pages/books.html", AllItems)


def update(request, id):
    # Get Item Of Id
    book_id = Book.objects.get(id=id)
    if request.method == "POST":
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect("/")
    else:
        book_save = BookForm(instance=book_id)
    # كل المنتجات
    AllItems = {
        "itemUpdate": book_save,
    }
    return render(request, "pages/update.html", AllItems)


def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book_delete.delete()
        return redirect("/")
    return render(request, "pages/delete.html")
