from rest_framework import serializers
from .models import Recipes
# from django.contrib.auth.models import User


class RecopesSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Recipes
        fields = ('recipe_id', 'recipe_name', 'how_to_cook', 'time_cook', 'ingredient')

    def perform_create(self, serializer):
        serializer.save()