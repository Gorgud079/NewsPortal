from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from NewsPortal.models import Author
# from ..NewsPortal.models import Category
from django.contrib.auth.decorators import login_required


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    template_name = 'signup.html'
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    common_group = Group.objects.get(name='common')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
        Author.objects.create(user_id=user.id, rating=0)
        if not request.user.groups.filter(name='common').exists():
            common_group.user_set.add(user)
    return redirect('/')


def subscribe_me(request):
    return redirect('/')
#     user = request.user
#     sport_subscribe = Category.objects.get(name='спорт')
#     politica_subscribe = Category.objects.get(name='политика')
#     finance_subscribe = Category.objects.get(name='финансы')
#     education_subscribe = Category.objects.get(name='образование')
#     if request.user.categories.get(sport_subscribe):
#         category.subscribes