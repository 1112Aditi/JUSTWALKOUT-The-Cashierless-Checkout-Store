from django.contrib import admin
from .models import *
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display=(
        'face_id',
        'name',
        'phone',
      
        'email',
        'balance',
    )
admin.site.register(UserProfile)