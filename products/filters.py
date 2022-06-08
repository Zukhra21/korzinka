import django_filters
from django_filters import NumberFilter, CharFilter
from .models import *
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields= '__all__'
        exclude = ['productCode','description', 'date_created']