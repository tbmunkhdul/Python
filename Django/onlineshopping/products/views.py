from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import Product, Category
from carts.models import Cart, CartItem

def home(request):
    selected_category = request.path
    page = request.GET.get('page')
    cartitems = None

    if str(selected_category).split('/')[-1]:
        categoryname = str(selected_category).split('/')[-1]
        catId = Category.objects.get(category_name=categoryname)
        product_list = Product.objects.filter(product_category_id=catId.id)
    elif 'squery' in request.GET:
        print(request.GET)
        squery = request.GET['squery']
        product_list = Product.objects.filter(product_name__icontains=squery)
    else:
        product_list = Product.objects.order_by('?')

    paginator = Paginator(product_list, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    
    if str(request.user) is not "AnonymousUser":
        # cartitems = Cart.objects.filter(user_id=int(request.user.id)).count()
        cartitems = Cart.objects.filter(user_id=int(request.user.id))
    
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories, 'cartitems':cartitems})

    
def productdetail(request, productid):
    cartitems = None
    
    if str(request.user) is not "AnonymousUser":
        # cartitems = Cart.objects.filter(user_id=int(request.user.id)).count()
        cartitems = Cart.objects.filter(user_id=int(request.user.id))
    
    product = Product.objects.filter(id=productid)
    categories = Category.objects.all()
    return render(request, 'productdetail.html', {'products': product, 'categories': categories, 'cartitems':cartitems})

def mycart(request):
    page = request.GET.get('page')
    cartitems = None

    product_list = Product.objects.filter(cartitem__cart__user=request.user)

    paginator = Paginator(product_list, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    
    if str(request.user) is not "AnonymousUser":
        cartitems = Cart.objects.filter(user_id=int(request.user.id))
    
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories, 'cartitems':cartitems})
