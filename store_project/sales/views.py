from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from inventory.models import Product
from .models import Order

#Shoppage
def shop(request):
    products=Product.objects.all()
    return render(request,'sales/shop.html',{'products': products})

#Buyproduct
def buy_product(request, pk):
    product=get_object_or_404(Product,pk=pk)
    if product.stock <= 0:
        messages.error(request, "Product is out of stock!")
        return redirect('shop')
    quantity=1
    total=product.price * quantity
    Order.objects.create(
        customer=request.user,
        product=product,
        quantity=quantity,
        total_price=total
    )
    product.stock-=quantity
    product.save()
    messages.success(request,"Product purchased successfully!")
    return redirect('shop')