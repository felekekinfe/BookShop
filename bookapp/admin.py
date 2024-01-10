from django.contrib import admin
from .models import Item,Order,OrderItem
# Register your models here.

admin.site.register(Order)


@admin.register(Item)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("title", "price","category","label")



@admin.register(OrderItem)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user", "quantity","item",)