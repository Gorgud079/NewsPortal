from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = 'post_rating'
    template_name = 'news.html'
    context_object_name = 'news'
