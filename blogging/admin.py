from django.contrib import admin
from .models import Post
# Register your models here.



class AdminPost(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'content']

admin.site.register(Post, AdminPost)