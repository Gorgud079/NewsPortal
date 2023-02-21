from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from datetime import datetime
# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
    permission_required = ('news.add_post',)


    def form_valid(self, form):
        post = form.save(commit=False)
        if 'news' in self.request.path.split('/'):
            post.position = "NS"
            self.template_name = 'news_create.html'
            self.success_url = reverse_lazy('news_create')
        else:
            post.position = "AE"
            self.template_name = 'art_create.html'
            self.success_url = reverse_lazy('art_create')
        return super().form_valid(form), self.template_name


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class CommentView(DetailView):
    model = Comment
    template_name = 'post.html'
    context_object_name = 'comment'
