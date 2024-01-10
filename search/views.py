from django.shortcuts import render

# Create your views here.

# views.py
from django.shortcuts import render
from bookapp.models import Item

def search_book(request):
    query = request.GET.get('query', '')
    
    if query:
        books = Item.objects.filter(title__icontains=query)
    else:
        books = Item.objects.all()

    return render(request, 'search_page.html', {'query': query, 'books': books})
