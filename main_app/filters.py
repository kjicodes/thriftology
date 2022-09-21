import django_filters
from .models import Listing
from django_filters import CharFilter, ChoiceFilter

SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('X', 'X-Large')
)

GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('U', 'Unisex')
)

CONDITION_CHOICES = (
    ('N', 'New'),
    ('L', 'Like New'),
    ('G', 'Good'),
    ('F', 'Fair')
)

class ListingFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')
    description = CharFilter(field_name="description", lookup_expr='icontains')
    size = ChoiceFilter(choices = SIZES)
    gender = ChoiceFilter(choices = GENDER_CHOICES)
    condition = ChoiceFilter(choices = CONDITION_CHOICES)


    class Meta:
        model = Listing
        fields = ['title', 'description', 'size', 'gender', 'condition']
        