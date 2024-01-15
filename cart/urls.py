from django.urls import path
from .views import add_to_cart,remove_from_cart,remove_single_book_from_cart,add_single_book_to_cart

urlpatterns = [
    path('add-single-book/<int:pk>',add_single_book_to_cart,name='add-single-book'),
    path('remove-single-book/<int:pk>',remove_single_book_from_cart,name='remove-single-book'),
    path('add-to-cart/<int:pk>',add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<int:pk>',remove_from_cart,name='remove-from-cart')
]
