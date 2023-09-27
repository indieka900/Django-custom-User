from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Course, CourseCategories

class UserAdminConfig(UserAdmin):
    ordering = ('-date_joined',)
    search_fields = ('email','full_name',)
    list_filter = ('email','is_active','is_staff',)
    list_display = ('id','email','full_name','phone_number','is_staff')
    fieldsets = (
        (None, {'fields': ('email','full_name','phone_number',)}),
        ("Permissions", {"fields" :('is_staff','is_active','is_superuser')}),
        ("Personal", {"fields":("avatar","image")}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('email','full_name','password1','password2','phone_number','is_staff','is_active','is_superuser','image')
        }),
    )

admin.site.register(CustomUser,UserAdminConfig)
admin.site.register(Course)
admin.site.register(CourseCategories)

# Register your models here.
