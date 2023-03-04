from django.urls import path
from .views import IndexView, IndexView1

urlpatterns = [
    path('', IndexView.as_view()),
    path('', IndexView1.as_view()),

]