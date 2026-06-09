from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, BloodRequest, Donor

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'groups', 'user_permissions')}),
    )
    
   
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()


class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'blood_group', 'city', 'hospital_name', 'contact_number', 'date')
    list_filter = ('blood_group', 'city', 'date')
    search_fields = ('patient_name', 'hospital_name', 'contact_number')
    ordering = ('-date',)


class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'blood_group', 'email', 'city', 'created_at')
    list_filter = ('blood_group', 'city', 'created_at')
    search_fields = ('name', 'email', 'city')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(BloodRequest, BloodRequestAdmin)
admin.site.register(Donor, DonorAdmin)