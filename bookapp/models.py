from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.urls import reverse
from django_countries.fields import CountryField
import uuid


CATEGORY=(
    ('Fiction','Fiction'),
    ('Science & Technology','Science & Technology'),
    ('Poetry','Poetry'),
    ('History','History'),
    ('Polotics','Polotics'),
    ('Philosophy','Philosophy'),
    ('Psycology','Psycology'),
    ('Self Help','Self Help')
)




# Create your models here.
class Item(models.Model):
    
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)

    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True,null=True)
    category=models.CharField(choices=CATEGORY, max_length=100)

    image=models.ImageField(upload_to='book_image/')

    def __str__(self):
        return self.title
    
    # def get_add_to_cart_url(self):
    #     return reverse('add-to-cart', kwargs={'pk':id})

    # def get_remove_from_cart_url(self):
    #     return reverse('remove_from_cart', kwargs={'pk':id})
    
    

class OrderItem(models.Model):
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    
    

    

    def __str__(self):
        return self.item.title
    
    def total_discount(self):
        return self.quantity*self.item.discount_price
    def total_price(self):
        return self.item.price * self.quantity-self.total_discount()
    

 

class Order(models.Model):
    
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField(auto_now_add=True)
    ordered=models.BooleanField(default=False)
    #billing_address=models.ForeignKey("BillingAddress", on_delete=models.SET_NULL, blank=True,null=True)

    
    def __str__(self):
        return self.user.username
    
    def trx(self):
        unique_number = uuid.uuid4()

        return unique_number


    
    


    def over_all_total_price(self):
        total=0
        for order_book in self.items.all():
            total+=order_book.total_price()

        return total






# class BillingAddress(models.Model):
#     user=models.ForeignKey(Account, on_delete=models.CASCADE)




#     street_address=models.CharField(max_length=100)
#     house_address=models.CharField(max_length=100)
#     countries=CountryField(multiple=True)
#     zip_code=models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username











































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































    