from rest_framework import serializers
from .models import CustomUser,Course

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['groups','user_permissions']
        
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        # exclude = ['groups','user_permissions']
