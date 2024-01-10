from django.urls import path
from .views import HomeVeiws,BookDetail




urlpatterns = [

    path('',HomeVeiws.as_view(),name='home'),
    path('book-detail/<int:pk>',BookDetail.as_view(),name='book-detail'),
   
]
