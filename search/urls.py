from django.urls import path
from search.views import search_book
urlpatterns = [
    path('search_book',search_book,name='search_book'),
    
]
