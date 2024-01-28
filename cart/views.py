from django.shortcuts import render,get_object_or_404
from bookapp.models import Item,Order,OrderItem
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages

# Create your views here.

# import logging

# def add_to_cart(request, pk):
#     try:
#         item = get_object_or_404(Item, id=pk)
#         order_item, created = OrderItem.objects.get_or_create(
#             item=item,
#             user=request.user,
#             ordered=False,
#         )
#         order_qs = Order.objects.filter(user=request.user, ordered=False)

#         if order_qs.exists():
#             order = order_qs[0]
#             # Check if the order item is in the order
#             if order.items.filter(item__id=item.id, ordered=False).exists():
#                 existing_order_item = OrderItem.objects.get(item=item, user=request.user, ordered=False)
#                 existing_order_item.quantity += 1
#                 existing_order_item.save()
#                 print("Quantity incremented for existing item.")
#             else:
#                 order.items.add(order_item)
#                 print("New item added to the order.")
#         else:
#             order_date = timezone.now()
#             order = Order.objects.create(user=request.user, ordered_date=order_date)
#             order.items.add(order_item)
#             print("New order created with item.")

#         print(f"Final quantity for item {item.id}: {order_item.quantity}")
#         return redirect('book-detail', pk=pk)
#     except Exception as e:
#         logging.exception("Error in add_to_cart:")
#         return redirect('book-detail', pk=pk)  # You can modify this to handle errors appropriately in your application

    
def add_to_cart(request, pk):
    item = get_object_or_404(Item, id=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order
        if order.items.filter(item__id=item.id, ordered=False).exists():
            existing_order_item = OrderItem.objects.get(item=item, user=request.user, ordered=False)
            existing_order_item.quantity += 1
            existing_order_item.save()
            messages.info(request, "Book Quantity Updated!")
            
        else:
            messages.info(request, "Book Added to Your Cart!")
            order.items.add(order_item)
            
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=order_date)
        order.items.add(order_item)
        messages.info(request, "Book Added to Your Cart!")

    #print(f"Final quantity for item {item.id}: {order_item.quantity}")
    return redirect('home')


def remove_from_cart(request,pk):
    item=get_object_or_404(Item,id=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
       
    #check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False)[0]

            order.items.remove(order_item)
            messages.info(request, "Book Removed From Your Cart!")
            return redirect('order_summary')
        else:
            messages.info(request, "This Book Was Not In Your Cart!")

            return redirect('book-detail',pk=pk)
    else:
        messages.info(request, "You Dont Have an Active Order!")
        return redirect('book-detail',pk=pk)

    return redirect('book-detail',pk=pk)

def remove_single_book_from_cart(request,pk):
    item=get_object_or_404(Item,id=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
       
    #check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item=OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False)[0]
            if order_item.quantity>1:

                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item) 
            messages.info(request, "Book quantity was updated !")
            return redirect('order_summary')

        else:
            messages.info(request, "This Book Was Not In Your Cart!")

            return redirect('book-detail',pk=pk)
    else:
        messages.info(request, "You Dont Have an Active Order!")
        return redirect('book-detail',pk=pk)

    return redirect('book-detail',pk=pk)



def add_single_book_to_cart(request,pk):
    item=get_object_or_404(Item,id=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
       
    #check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item=OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]

            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Book quantity was updated !")
            return redirect('order_summary')

        else:
            messages.info(request, "This Book Was Not In Your Cart!")

            return redirect('book-detail',pk=pk)
    else:
        messages.info(request, "You Dont Have an Active Order!")
        return redirect('book-detail',pk=pk)

    return redirect('book-detail',pk=pk)