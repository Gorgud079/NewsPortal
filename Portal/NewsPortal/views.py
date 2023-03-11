from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category, Subscribe
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from datetime import datetime


class PostsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class CategoryList(ListView):
    model = Category
    template_name = "category.html"
    context_object_name = "category"
    paginate_by = 10


class SubscribeList(ListView):
    model = Post
    template_name = 'politicaNews.html'
    context_object_name = 'sub'
    paginate_by = 20


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


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
    permission_required = ('NewsPortal.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        if 'news' in self.request.path:
            post.position = "NS"
            self.template_name = 'news_create.html'
            self.success_url = reverse_lazy('news_create')
        else:
            post.position = "AE"
            self.template_name = 'art_create.html'
            self.success_url = reverse_lazy('art_create')
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('NewsPortal.change_post',)


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    permission_required = ('NewsPortal.delete_post',)


class CommentView(DetailView):
    model = Comment
    template_name = 'post.html'
    context_object_name = 'comment'

@login_required
def subscribe_category(request):
    user = request.user
    path = request.META["HTTP_REFERER"]
    id = path.split("/")[-1]
    post = Post.objects.filter(pk=id)
    if 1 == int(post.values('categories')[0]['categories']):
        if not Subscribe.objects.filter(category_current_id=1, user_current_id=user.id):
            Subscribe.objects.create(category_current_id=1, user_current_id=user.id)
        return redirect('http://127.0.0.1:8000/categories/sport/')
    elif 2 == int(post.values('categories')[0]['categories']):
        if not Subscribe.objects.filter(category_current_id=2, user_current_id=user.id):
            Subscribe.objects.create(category_current_id=2, user_current_id=user.id)
        return redirect('http://127.0.0.1:8000/categories/politics/')
    elif 3 == int(post.values('categories')[0]['categories']):
        if not Subscribe.objects.filter(category_current_id=3, user_current_id=user.id):
            Subscribe.objects.create(category_current_id=3, user_current_id=user.id)
        return redirect('http://127.0.0.1:8000/categories/education/')
    elif 4 == int(post.values('categories')[0]['categories']):
        if not Subscribe.objects.filter(category_current_id=4, user_current_id=user.id):
            Subscribe.objects.create(category_current_id=4, user_current_id=user.id)
        return redirect('http://127.0.0.1:8000/categories/finance/')
    return redirect('http://127.0.0.1:8000/categories/')

