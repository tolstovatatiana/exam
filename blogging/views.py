from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    fields = ['id', 'title']
    template_name = 'home.html'