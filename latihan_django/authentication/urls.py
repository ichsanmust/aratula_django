from django.urls import path
from authentication.views import RegisterView, LoginView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('sign-in', LoginView.as_view()),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign-up', RegisterView.as_view(), name='auth_register'),
]