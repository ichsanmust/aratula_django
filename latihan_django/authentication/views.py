# from django.contrib.auth.models import User
from .models import Users
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta,datetime
from rest_framework import status


class RegisterView(generics.CreateAPIView):
    # queryset = User.objects.all()
    queryset = Users.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'Message' : 'User '+ response.data['username']+' registered successfully',
            'status' : 'success',
            'statusCode': 200,
            'data': response.data
        })

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # login(request, user)
            token = generate_jwt_token(user)
            return Response(
                {
                    "username" : user.username,
                    "token": token,
                    "message": "Login berhasil!",
                    'status' : 'success',
                    'statusCode': 200,
                }, 
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def generate_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    refresh['user_id'] = user.user_id
    refresh['id'] = user.user_id

    # expired_time = datetime.now() + timedelta(days=1)
    # expired_formatted = expired_time.strftime("%d/%m/%Y %H:%M:%S")

    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
        # 'expired' : expired_formatted
    }
