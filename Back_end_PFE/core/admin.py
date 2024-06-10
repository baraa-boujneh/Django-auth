from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','is_staff','is_active',
                    'is_superuser','date_joined','last_login')
admin.site.register(User, CustomUserAdmin)
