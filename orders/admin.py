from django.contrib import admin

from orders.models import Customer, Order

admin.site.register(Customer)
admin.site.register(Order)
# Register your models here.
