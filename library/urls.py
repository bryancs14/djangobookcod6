"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from rest_framework import routers
from catalog import views, viewsets

router = routers.DefaultRouter()
router.register('books', viewsets.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^catalog/[\/]?$', views.catalog_list),
    # Apis
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace = 'rest_framework')),

    path('catalog/books', views.new_book),
    path('catalog/book/<pk>/update', views.update_book),

    # path('books', views.BookCreate.as_view()),
    # path('book/<pk>', views.BookUpdate.as_view()),
    path('authors', views.AuthorCreate.as_view()),
    path('authors/list', views.AuthorsList.as_view()),

    
    # catalog/<editorial>/books?year=2020

    # Con expresiones regulares
    # re_path(r'catalog\/(?P<editorial>[a-zA-Z]+)\/books', views.get_books_by_editorial),
    path('catalog/<editorial>/books', views.get_books_by_editorial)
]
