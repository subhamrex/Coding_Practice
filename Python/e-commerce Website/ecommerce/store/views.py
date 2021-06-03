from django.shortcuts import render
from django.http import JsonResponse # Add json response
#import models in views
import json
import datetime
from .models import *
# Create your views here.
#2. Add your views

def store(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]    
        order = {'get_cart_total':0,'get_cart_items':0,'shippingProduct':False}
        cartItems = order['get_cart_items']
        
    products = Product.objects.all()
    context ={'products': products,'cartItems':cartItems }
    return render (request,'store.html',context)

def cart(request):
    #Authenticated user 
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]    
        order = {'get_cart_total':0,'get_cart_items':0,'shippingProduct':False}
        cartItems = order['get_cart_items']
    context ={'items':items,'order':order,'cartItems':cartItems}
    return render (request,'cart.html',context)

def checkout(request):
    #At Checkout page we need same data as cart 
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]    
        order = {'get_cart_total':0,'get_cart_items':0,'shippingProduct':False}
        cartItems = order['get_cart_items']
    context ={'items':items,'order':order,'cartItems':cartItems}
    return render (request,'checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('productId:',productId)
    print('action:',action)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,completed=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order = order,product=product)
    
    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()    
    
    if orderItem.quantity <=0:
        orderItem.delete()
        
            
    return JsonResponse('Item was added',safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    #print('Data:',request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False) 
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        if total == order.get_cart_total:
            order.completed = True
        order.save()  
        
        if order.shippingProduct == True:
            Shipping.objects.create(
                customer=customer,
                order=order,
                address=data['shippingProduct']['address'],
                city = data['shippingProduct']['city'],
                state = data['shippingProduct']['state'],
                zipcode=data['shippingProduct']['zipcode'],
                                           )
    else:
        print('User is not logged in...')    
    return JsonResponse('Payment complete!',safe=False)