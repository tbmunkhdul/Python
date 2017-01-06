from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    
    def __str__(self):
        return '{}'.format(self.user)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True)
    product = models.ForeignKey(Product)
    
    def __str__(self):
        return '{}'.format(self.product)





