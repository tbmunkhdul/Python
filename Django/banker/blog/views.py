from django.shortcuts import render
from blog.models import Blog, Catergories
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import context

def showAllblogs(request):
    number_of_blogs = None
    squery = None
    page = request.GET.get('page')
    
    if 'squery' in request.GET:
        squery = request.GET['squery']
        blogs_list = Blog.objects.filter(blog_short__icontains=squery)
        number_of_blogs = True
    elif request.GET.get('cat'):
        blogs_list = Blog.objects.filter(blog_cate_id=request.GET.get('cat'))
    else:    
        blogs_list = Blog.objects.all()

    paginator = Paginator(blogs_list, 3)  # Show 3    
   

    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    categories = Catergories.objects.all()
    return render(request, 'index.html', {'blogs': blogs, 'number_of_blogs':number_of_blogs,
                                          'squery':squery, 'categories': categories})

def readMore(request, blogId):
    blog = Blog.objects.filter(id__icontains=blogId)
    return render(request, 'readmore.html', {'blog': blog})



