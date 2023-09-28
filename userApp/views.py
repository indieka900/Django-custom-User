from rest_framework.views import APIView
from .models import CustomUser, Course
from .serializers import CustomUserSerializer,CourseSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_lesson(request):

    if not request.user.is_authenticated:
        queryset = Course.objects.all() 
        serializer_class = CourseSerializer(queryset,many=True)
        return Response(serializer_class.data)

    return Response({"Error":"Not allowed"})
            

class CustomUserList(APIView):
    def get(self, request):
        queryset = CustomUser.objects.all() 
        serializer_class = CustomUserSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    
    def post(self, request): 
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')

            # Check if the user exists in the database.
            user = CustomUser.objects.filter(email=email).first()

            # If the user exists, authenticate them and log them in.
            if user:
                if authenticate(request, email=email, password=password):
                    login(request, user)

                    # Generate a refresh token and access token for the user.
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)

                    # Serialize the user data.
                    serializer = CustomUserSerializer(user)

                    # Return the response.
                    response_data = {
                        'Status': True,
                        'message': 'User logged in succesfully',
                        'token': access_token,
                        'user': serializer.data
                    }
                    return Response(response_data, status=200)
                else:
                    return Response({'message': 'Invalid credentials'}, status=400)
            else:
                # The user does not exist in the database, so register them.
                serializer = CustomUserSerializer(data=request.data)
                if serializer.is_valid():
                    if password:
                        hashed_pass = make_password(password)
                        serializer.validated_data['password'] = hashed_pass

                    serializer.save()

                    response_data = {
                        'Status': True,
                        'message': 'User created succesfully',
                        'user': serializer.data
                    }
                    return Response(response_data, status=200)
                else:
                    return Response(serializer.errors, status=400)
