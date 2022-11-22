from apps.places.models import Location, LocationName, LocationFeature
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

class LocationFeatureSerializer(serializers.ModelSerializer):
  # Include the lat/long fields from the location so the feature can be mapped.
  location = LocationSerializer(many=False, read_only=True)
  class Meta:
        model = LocationFeature
        fields = [
          'location_feature_key',
          'item_name',
          'comment',
          'location_key',
          'feature_grading_key',
          'date_from',
          'date_to',
          'location',
        ]
        depth = 1