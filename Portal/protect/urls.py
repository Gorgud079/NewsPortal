from django.urls import path
from .views import IndexView, IndexView1

urlpatterns = [
    path('', IndexView.as_view()),
    path('news', IndexView1.as_view()),

]