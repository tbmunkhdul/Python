from django.http import HttpResponse

def default(request):
    return HttpResponse('Page not found, please <a href="./blog">click on </a>')