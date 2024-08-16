from rest_framework import filters


class RecipesOrder(filters.OrderingFilter):
    ordering_param = 'sortBy'