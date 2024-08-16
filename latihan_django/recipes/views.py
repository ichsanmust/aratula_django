from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Recipes
# from .permissions import IsOwnerOrReadOnly
from .serializers import RecopesSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from django_filters.rest_framework import DjangoFilterBackend
from . import orders
from rest_framework.response import Response
from rest_framework import status



# class ListCreateRecipesAPIView(ListCreateAPIView):
#     serializer_class = RecopesSerializer
#     queryset = Recipes.objects.all()
#     # permission_classes = [IsAuthenticated]
#     pagination_class = CustomPagination
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = MovieFilter

#     def perform_create(self, serializer):
#         # Assign the user who created the movie
#         serializer.save()


class ListCreateRecipesAPIView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Recipes.objects.all()
    serializer_class = RecopesSerializer
    filter_backends = [DjangoFilterBackend,orders.RecipesOrder]
    filterset_fields = ['recipe_id', 'recipe_name', 'how_to_cook', 'time_cook', 'ingredient']
    filterset_class = MovieFilter
    ordering_fields = ['recipe_id', 'recipe_name', 'how_to_cook', 'time_cook', 'ingredient']
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {
            'data': serializer.data,
            'message': 'Success Insert data',
            'statusCode': 200,
            'status': 'Success'
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class RetrieveUpdateDestroyRecipesAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecopesSerializer
    queryset = Recipes.objects.all()
    # permission_classes = [IsAuthenticated]