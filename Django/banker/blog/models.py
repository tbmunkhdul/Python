from django.db import models


class Catergories(models.Model):
    cat_title = models.CharField(max_length=255)
    
    def __str__(self):
        return '{}'.format(self.cat_title)
    
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_short = models.CharField(max_length=255)
    blog_date = models.DateTimeField()
    blog_content = models.TextField()
    blog_pic = models.FileField(upload_to='documents/%Y/%m/%d')
    blog_cate = models.ForeignKey(Catergories, null=True, related_name='ct')
    
    def __str__(self):
        return '{}'.format(self.blog_title)
    

