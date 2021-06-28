from django.contrib import admin

# Register your models here.
from .models import Location, LocationName, LocationType

@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = (
      'short_name',
      'long_name',
      'description',
    )

class LocationNameInline(admin.TabularInline):
    model = LocationName

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        LocationNameInline,
    ]
    search_fields = [
        'names__item_name',
    ]