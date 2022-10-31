from django.contrib import admin

# Register your models here.
from .models import Location, LocationAdminArea, LocationName, LocationType

@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = (
      'short_name',
      'long_name',
      'description',
    )

class LocationNameInline(admin.TabularInline):
    model = LocationName

class LocationAdminAreaInline(admin.TabularInline):
    model = LocationAdminArea

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        LocationNameInline,
        LocationAdminAreaInline,
    ]
    search_fields = [
        'names__item_name',
    ]