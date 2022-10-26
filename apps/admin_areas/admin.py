from django.contrib import admin

# Register your models here.
from .models import AdminArea, AdminType

@admin.register(AdminArea)
class AdminAreaAdmin(admin.ModelAdmin):
    list_display = (
      'item_name',
      'admin_type_key',
      'short_code',
    )

@admin.register(AdminType)
class AdminTypeAdmin(admin.ModelAdmin):
    list_display = (
        'short_name',
        'long_name',
        'description',
    )