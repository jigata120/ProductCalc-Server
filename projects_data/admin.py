# myapp/admin.py


from .models import  Project


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile

class UserProfileAdmin(BaseUserAdmin):
    model = UserProfile
    list_display = ('email', 'name', 'role', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'profile_url', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'final_product', 'owner')
    list_filter = ('final_product', 'owner')
    search_fields = ('title', 'owner__name')
    filter_horizontal = ('members',)

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Project, ProjectAdmin)