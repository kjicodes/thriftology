import django_filters
from .models import Listing
from django_filters import CharFilter

class ListingFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')
    size = CharFilter(field_name="size", lookup_expr='icontains')
    gender = CharFilter(field_name="gender", lookup_expr='icontains')


    class Meta:
        model = Listing
        fields = ['title', 'size', 'gender']
        