from django.urls import path
from .views import HomeVeiws,BookDetail,about_us




urlpatterns = [

    path('',HomeVeiws.as_view(),name='home'),
    path('aboutUs/',about_us,name='about-us'),
    path('book-detail/<int:pk>',BookDetail.as_view(),name='book-detail'),
   
]
