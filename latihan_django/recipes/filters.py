from django_filters import rest_framework as filters
from .models import Recipes


# We create filters for each field we want to be able to filter on
class MovieFilter(filters.FilterSet):
    recipe_id = filters.CharFilter(lookup_expr='icontains')
    recipe_name = filters.CharFilter(lookup_expr='icontains')
    how_to_cook = filters.CharFilter(lookup_expr='icontains')
    time_cook = filters.NumberFilter()
    ingredient = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Recipes
        fields = ('recipe_id', 'recipe_name', 'how_to_cook', 'time_cook', 'ingredient')
