from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'first_name', 'last_name', 'email', 'role', 'phone', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active', 'is_staff', 'role')
    fields = ('staff_id', 'first_name', 'last_name', 'email', 'role', 'phone', 'address', 'is_active', 'is_staff')
    readonly_fields = ('staff_id',)

admin.site.register(User, UserAdmin)