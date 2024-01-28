from django.contrib import admin
from .models import Item, Order, OrderItem, Account

# Define your custom admin classes
class AccountAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","phone")  # Add custom admin options here

class OrderAdmin(admin.ModelAdmin):
    list_display = ("user","ordered")  # Add custom admin options here



class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category",)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("user", "quantity", "item")

# Custom AdminSite
class CustomAdminSite(admin.AdminSite):
    site_header = 'BookShop Administration Page'

   

# Instantiate the custom admin site
custom_admin_site = CustomAdminSite(name='customadmin')

# Register your models with the custom admin site
custom_admin_site.register(Account, AccountAdmin)
custom_admin_site.register(Order, OrderAdmin)

custom_admin_site.register(Item, ItemAdmin)
custom_admin_site.register(OrderItem, OrderItemAdmin)




