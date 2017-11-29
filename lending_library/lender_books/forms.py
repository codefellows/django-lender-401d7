from django import forms
from lender_books.models import Book


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = []
