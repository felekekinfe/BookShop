from django.shortcuts import render,get_object_or_404
from .models import Item,OrderItem,Order
from django.shortcuts import redirect

from django.views.generic import ListView,DetailView
# Create your views here.

class HomeVeiws(ListView):
    model=Item
    paginate_by=4
    template_name="home-page.html"
    context_object_name='items'
    def get_queryset(self):
        return Item.objects.all()
    
class BookDetail(DetailView):
    model=Item
    template_name="book_detail.html"
def about_us(request):
    return render(request, 'aboutus.html')

def check_out(request):
    return render(request, 'checkout-page.html')

# def add_to_cart(request,pk):
#     item=get_object_or_404(Item,id=pk)
#     order_item=OrderItem.objects.create(item=item)
#     order_qs=Order.objects.filter(user=request.user,ordered=False)

#     if order_qs.exists():
#         order=order_qs[0]
#         #check if the order item is in the order
#         if order.items.filter(id=item.id):
#             order_item.quantity+=1
#             order_item.save()
#     else:
#         order=Order.objects.create(user=request.user)
#         order.items.add(order_item)
    
#     return redirect('book-detail',kwargs={'pk':pk})
    