from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import Product, Category

def home(request):
    selected_category = request.path
    page = request.GET.get('page')

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

    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

    

