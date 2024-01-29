from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from bookapp.models import Item
from django.contrib import messages

def search_book(request):
    query = request.GET.get('query', '')

    if query:
        books = Item.objects.filter(
            Q(title__icontains=query) | 
            Q(author=query) | 
            Q(category=query)

        )
        paginator = Paginator(books, 2)  # Show 10 books per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'search_page.html', {'books': books, 'page_obj': page_obj})
        
    else:
       
         # or a subset, e.g., Item.objects.none()

    # Pagination
     

        return render(request, 'search_page.html')
