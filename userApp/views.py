from rest_framework import generics
from .models import CustomUser  # Replace with your User model import
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            # token, created = Token.objects.get_or_create(user=user)
            return Response({'token': 'token.key'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()  # Replace with your User model
    serializer_class = CustomUserSerializer
