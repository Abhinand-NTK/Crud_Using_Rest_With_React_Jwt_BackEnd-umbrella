from django.contrib import admin
from .models import UserAccount
@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','is_active','is_staff')