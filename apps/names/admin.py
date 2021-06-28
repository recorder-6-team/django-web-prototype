from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
      'username',
      'security_level',
      'first_login',
      'full_edit_own_data',
      'last_login',
    )
    search_fields = (
      'security_level',
      'last_login',
      'username',
    )
    ordering = (
      'security_level',
      'last_login',
      'username',
    )
    list_filter = (
      'security_level',
    )
    filter_horizontal = ()
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile',)}),
    )

    def staff(self, obj):
        return self.security_level >= 4

    def superuser(self, obj):
        return self.security_level >= 5
