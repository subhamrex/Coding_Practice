from django.db import models
from django.contrib.auth.models import User  # Add default user in django
# Create your models here.


class Customer(models.Model):  # Add Customer model
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):  # Add Product model
    name = models.CharField(max_length=255)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class Order(models.Model):  # Add Order model
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shippingProduct(self):
        shippingProduct = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shippingProduct = True

        return shippingProduct

    @property
    def get_cart_total(self):  # Get total in cart
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):  # Get cart item
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):  # Add OrderItem
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)  # ......

    @property
    def get_total(self):  # Get total value of order items
        total = self.product.price * self.quantity
        return total


class Shipping(models.Model):  # Add Shipping
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL, blank=True)
    order = models.ForeignKey(
        Order, null=True, on_delete=models.SET_NULL, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
