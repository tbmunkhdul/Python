from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from products import views
from carts import cartviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^category/', views.home, name='home'),
    url(r'^mycart/$', views.mycart, name='mycart'),
    url(r'^productdetail/(\d+)/$', views.productdetail, name='productdetail'),
    url(r'^productdetail/(\d+)/addtocart/$', cartviews.addtocart),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
