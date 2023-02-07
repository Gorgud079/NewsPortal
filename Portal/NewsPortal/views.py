from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context

class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

