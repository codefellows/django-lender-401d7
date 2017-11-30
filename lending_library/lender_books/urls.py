from django.conf.urls import url
from lender_books.views import NewBookView, OneBook
from lender_books.models import Book


urlpatterns = [
    url(r'^new$', NewBookView.as_view(), name='new_book'),
    url(r'^(?P<slug>[\w\-\_]+)$', OneBook.as_view(), name='one_book_slug'),
    url(r'^(?P<pk>\d+)$', OneBook.as_view(
        model=Book,
        template_name='lender_books/book_detail.html',
        context_object_name='book'
    ), name='one_book_pk')
]