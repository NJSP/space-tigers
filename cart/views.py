from django.shortcuts import render, get_object_or_404, redirect
from space_tigersapp.models import Product
from cart.models import Cart

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    # Cap the quantity based on product stock
    if quantity > product.stock:
        quantity = product.stock

    cart.add(product=product, quantity=quantity)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    # Cap the quantity based on product stock
    if quantity > product.stock:
        quantity = product.stock

    cart.add(product=product, quantity=quantity, override_quantity=True)
    return redirect('cart:cart_detail')

def cart_buy(request):
    cart = Cart(request)

    # Loop through each item in the cart
    for item in cart:
        product = item['product']
        quantity = item['quantity']

        # Reduce the stock by the quantity purchased
        if product.stock >= quantity:
            product.stock -= quantity
            product.save()  # Save the updated stock to the database
        else:
            # Optionally, handle cases where stock is insufficient
            pass

    # Clear the cart after purchase
    cart.clear()

    # Redirect to the home page after purchase (temporarily)
    return redirect('index') 
