from django.contrib import admin
from .models import *
# Register your models here.
# Add my models

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)