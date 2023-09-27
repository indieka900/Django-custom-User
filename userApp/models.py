from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import FileExtensionValidator as _
import os
import subprocess

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='uploads/',null=True)
    full_name = models.CharField(max_length=30,default='')
    phone_number = models.CharField(max_length=15,blank=True,null=True) 
    avatar = models.CharField(max_length=500, blank=True, null=True,)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def get_avatar_name(self):
        if self.image:
            return self.image.name
        else:
            return None
        
    def get_short_name(self):
        if (len(self.full_name) == 0):
            return self.email.split('@')[0].capitalize()
        
        else:
            return self.full_name.split(' ')[0]


class CourseCategories(models.Model):
    title = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=300)
    order = models.SmallIntegerField()
    
    def __str__(self):
        return self.title       
        
class Course(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=1000,blank=True,null=True)
    type_id = models.SmallIntegerField(null=True,blank=True)
    follow = models.IntegerField(null=True,blank=True)
    lesson_number = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    score = models.DecimalField(max_digits=2, decimal_places=2,null=True,blank=True)
    video_length = models.DecimalField(max_digits=10, decimal_places=2,default=5, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='images_uploaded',null=True,blank=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,blank=True,
        validators=[_(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    Teacher = models.ForeignKey(CustomUser,on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def calculate_video_length(self):
        """Calculates the length of the video file and stores it in the database."""

        video_path = self.video.path

        command = ['ffprobe', '-i', video_path, '-show_entries', 'format=duration']
        output = subprocess.check_output(command)

        duration = float(output.decode().split('=')[1])

        self.video_length = duration
        self.save()
