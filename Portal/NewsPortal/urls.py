from django.urls import path, include
from .views import PostsList, PostsDetail, PostCreate, PostUpdate, PostDelete, subscribe_category, CategoryList, SubscribeList

urlpatterns = [
    path('', include('protect.urls')),
    path("news/", PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostsDetail.as_view(), name='post_detail'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('article/create/', PostCreate.as_view(template_name="art_create.html"), name='art_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscribe/', subscribe_category),
    path('categories/', CategoryList.as_view(), name="all_cat"),
    path('categories/education/', SubscribeList.as_view(template_name='educationNews.html'), name='education'),
    path('categories/politics/', SubscribeList.as_view(template_name='politicaNews.html'), name='politics'),
    path('categories/sport/', SubscribeList.as_view(template_name='sportNews.html'), name='sport'),
    path('categories/finance/', SubscribeList.as_view(template_name='financeNews.html'), name='finance'),

]