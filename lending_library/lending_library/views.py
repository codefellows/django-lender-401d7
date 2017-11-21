# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render


def home_view(request, number=None):
    """View for the home page."""
    # template = loader.get_template('lending_library/home.html')
    # response_body = template.render({"potato": number})
    return render(request, 'lending_library/home.html', context={"potato": number})


def potato_view(request):
    return render(request, 'lending_library/potato.html')