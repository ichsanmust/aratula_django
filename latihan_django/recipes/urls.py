from django.urls import path
from . import views

urlpatterns = [
    path('book-recipes', views.ListCreateRecipesAPIView.as_view()),
    path('book-recipes/<int:pk>', views.RetrieveUpdateDestroyRecipesAPIView.as_view(), name='get_delete_update_recipes'),
]