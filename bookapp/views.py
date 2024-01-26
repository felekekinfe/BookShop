from django.shortcuts import render,get_object_or_404
from .models import Item,OrderItem,Order,BillingAddress
from django.shortcuts import redirect
from .forms import CheckoutForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,View
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

class CheckoutView(View,ObjectDoesNotExist):

    def get(self,*args,**kwargs):
        form=CheckoutForm()
        context={
            'form':form
        }
        return render(self.request, "checkout-page.html", context)
    def post(self,*args,**kwargs):
        form=CheckoutForm(self.request.POST or None)
        print(self.request.POST)
        
        try:
            order=Order.objects.get(user=self.request.user,ordered=False)
            print(order)
            print(self.request.user.username)
            if form.is_valid():
                
                street_address=form.cleaned_data.get('street_address')
                house_address=form.cleaned_data.get('house_address')
                country=form.cleaned_data.get('country')
                zip_code=form.cleaned_data.get('zip_code')
                # same_billing_address=form.cleaned_data.get('same_billing_address')
                # save_info=form.cleaned_data.get('save_info')
                payment_option=form.cleaned_data.get('payment_option')
                billing_address=BillingAddress(
                    user=self.request.user,
                    street_address=street_address,
                    house_address=house_address,
                    countries=country,
                    zip_code=zip_code

                )
               
                
                billing_address.save()
                order.billing_address=billing_address
                order.save()
                print(street_address)
                """todo"""
                #take to payment page based on the selected payment option by passing it as parameter eg payment/y or p
                #if payement_option is p:
                    #redirect to payment/p
               # else:
                     #redirect to payment/y
                return redirect('checkout')

            messages.warning(self.request, "Failed checkout")
            return redirect('checkout')
            
        except ObjectDoesNotExist():
            messages.error(self.request,'you dont have active order')
            return redirect('order_summary')
        

class PaymentView(View):
    def get(self,*args,**kwargs):
        return render(self.request, "payment.html")


class OrderSummary(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        try:
            order=Order.objects.get(user=self.request.user,ordered=False)

            return render(self.request, 'order_summary.html',{'orders':order})
    
        except ObjectDoesNotExist():
            messages.error(self.request,'you dont have active order')

        
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
    