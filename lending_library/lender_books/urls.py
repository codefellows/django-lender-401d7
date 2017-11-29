from django.conf.urls import url
from lender_books.views import NewBookView


urlpatterns = [
    url(r'^new$', NewBookView.as_view(), name='new_book')
]