from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    date = DateFilter(widget=forms.DateInput(attrs={'type': 'date'}), lookup_expr='gt')
    class Meta:
        model = Post
        fields = ['headline', 'position', 'date']
        # fields = {
        #     'headline': ['icontains'],
        #     'position': ['icontains'],
        #     'time_in': ["gt"],
        # }

    # def __str__(self):
    #     return f"{self.date.strftime('%d-%m-%Y')}"
