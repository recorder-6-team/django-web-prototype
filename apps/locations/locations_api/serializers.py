from apps.locations.models import Location, LocationName
from rest_framework import serializers

class LocationNameSerializer(serializers.ModelSerializer):
  class Meta:
        model = LocationName
        fields = ['item_name', 'preferred']


class LocationSerializer(serializers.ModelSerializer):
  class Meta:
        model = Location
        fields = [
          'location_key',
          'description',
          'parent_key',
          'spatial_ref',
          'spatial_ref_system',
          'lat',
          'long',
          'location_type_key',
          'file_code',
          'names',
          'spatial_ref_qualifier',
          'approach',
          'restriction',
        ]
        depth = 1