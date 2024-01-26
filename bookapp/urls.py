from django.urls import path
from .views import HomeVeiws,BookDetail,about_us,OrderSummary,CheckoutView,PaymentView

from django.contrib import admin


urlpatterns = [
    
    path('',HomeVeiws.as_view(),name='home'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    path('order_summary',OrderSummary.as_view(),name='order_summary'),
    path('admin/', admin.site.urls,name='admin'),
    path('aboutUs/',about_us,name='about-us'),
    path('book-detail/<int:pk>',BookDetail.as_view(),name='book-detail'),

    path('payment/<payment_option>/',PaymentView.as_view(),name='payment')
   
]
