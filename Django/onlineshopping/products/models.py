from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    
    def __str__(self):
        return '{}'.format(self.category_name)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_desc = models.TextField()
    product_pic = models.FileField(upload_to='products/%Y/%m/%d')
    product_category = models.ForeignKey(Category, null=True, related_name='cat')
    
    def __str__(self):
        return '{}'.format(self.product_name)