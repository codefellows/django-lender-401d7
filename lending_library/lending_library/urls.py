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
from django.conf.urls import url#  , reverse <--- give it a url name and it'll print out the route
from django.conf.urls.static import static
from django.contrib import admin
from lending_library.views import home_view, potato_view
from lending_library import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^(?P<number>\d+)/$', home_view, name='variable'),
    url(r'^potato$', potato_view, name="potato")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)
