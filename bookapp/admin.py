from django.contrib import admin
from admin_interface.models import Theme
from .models import Item,Order,OrderItem,BillingAddress,Account
# Register your models here.

class CustomAdminSite(admin.AdminSite):
    site_header='Adminstration Page'
    
    index_template=''



custom=CustomAdminSite(name='customadmin')
custom.register(Account)
custom.register(Order)

@admin.register(BillingAddress)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("street_address",)

@admin.register(Item)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("title", "price","category","label")



@admin.register(OrderItem)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user", "quantity","item",)