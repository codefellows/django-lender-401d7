from django.shortcuts import render
from django.views.generic import CreateView
from lender_books.models import Book

# Create your views here.


class NewBookView(CreateView):
    model = Book
    template_name = 'lender_books/new_book.html'
    fields = ['cover_image', 'title', 'author', 'year', 'status']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
