from django.contrib import admin

# Register your models here.
from .models import Location
from .models import LocationAdminArea
from .models import LocationName
from .models import LocationType
from .models import TenureType

@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = (
      'short_name',
      'long_name',
      'description',
    )

@admin.register(TenureType)
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