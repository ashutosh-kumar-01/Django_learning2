from django.shortcuts import get_object_or_404, redirect, render

from .models import Book


def book_list(request):
    books = Book.objects.select_related('author').order_by('title')
    total = Book.objects.count()
    return render(request, 'library/books.html', {'books': books, 'total': total})


def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        try:
            year = int(request.POST['year'])
            if year > 0:
                book.publication_year = year
                book.save(update_fields=['publication_year'])
                return redirect('library:book_list')
        except (KeyError, TypeError, ValueError):
            pass
        return render(request, 'library/update.html', {
            'book': book,
            'error': 'Enter a valid publication year.',
        })

    return render(request, 'library/update.html', {'book': book})
