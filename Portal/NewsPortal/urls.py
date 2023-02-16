from django.urls import path
from .views import PostsList, PostsDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostsDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]