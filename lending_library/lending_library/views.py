# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from lender_books.models import Book


# def home_view(request, number=None):
#     """View for the home page."""
#     # template = loader.get_template('lending_library/home.html')
#     # response_body = template.render({"potato": number})
#     return render(request, 'lending_library/home.html', context={"potato": number})

# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'lending_library/home.html', {'objects': books})

class HomeView(TemplateView):
    template_name = 'lending_library/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['name'] = 'Fleeblegrap'
        return context


class BookListView(ListView):
    model = Book
    context_object_name = 'objects'
    template_name = 'lending_library/home.html'


def potato_view(request):
    return render(request, 'lending_library/potato.html')