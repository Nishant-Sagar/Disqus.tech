from django.contrib import admin
from .models import Post, Category
# from .models import QuillPost
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)

