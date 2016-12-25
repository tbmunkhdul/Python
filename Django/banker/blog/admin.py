from django.contrib import admin
from .models import Blog, Catergories

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_date', 'blog_cate')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Catergories)

