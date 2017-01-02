from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product, Category
from carts.models import Cart, CartItem

@login_required
def addtocart(request, productid):
    
    cartitems = None
    
    if str(request.user) is not "AnonymousUser":
        cartitems = Cart.objects.filter(user_id=int(request.user.id))
        
    product = Product.objects.filter(id=productid)
    categories = Category.objects.all()
    
    new_order = Cart()
    new_order.user = request.user
    new_order.save()
    
    new_order_product = CartItem()
    new_order_product.cart = new_order
    item_product = Product.objects.get(id=productid)
    new_order_product.product = item_product
    new_order_product.save()
    
    return render(request, 'cart.html', {'products': product, 'categories': categories, 'cartitems':cartitems})