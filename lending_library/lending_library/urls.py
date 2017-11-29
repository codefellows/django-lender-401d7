"""lending_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include#  , reverse <--- give it a url name and it'll print out the route
from django.conf.urls.static import static
from django.contrib import admin
from lending_library.views import BookListView, HomeView, potato_view
from lending_library import settings
from django.views.generic import ListView
from lender_books.models import Book

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', ListView.as_view(
    #     template_name='lending_library/home.html',
    #     model=Book
    # ), name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<number>\d+)/$', BookListView.as_view(), name='variable'),
    url(r'^potato$', potato_view, name="potato"),
    url(r'^books/', include('lender_books.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)
