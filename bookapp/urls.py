from django.urls import path
from .views import HomeVeiws,BookDetail,about_us,OrderSummary

from django.contrib import admin


urlpatterns = [

    path('',HomeVeiws.as_view(),name='home'),
    path('order_summary',OrderSummary.as_view(),name='order_summary'),
    path('admin/', admin.site.urls,name='admin'),
    path('aboutUs/',about_us,name='about-us'),
    path('book-detail/<int:pk>',BookDetail.as_view(),name='book-detail'),
   
]
