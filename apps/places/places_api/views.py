import django_filters.rest_framework
from .serializers import LocationSerializer, LocationFeatureSerializer
from rest_framework import viewsets
from rest_framework import permissions
from apps.places.models import Location, LocationName, LocationFeature

class LocationViewSet(viewsets.ModelViewSet):
    # Prefetch related location names so they can be included in response.
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
      'parent_key': ['exact', 'isnull'],
      'location_type_key': ['exact']
    }

    def get_queryset(self):
      queryset = Location.objects.all()
      # Ensure location names available without additional query.
      queryset = queryset.prefetch_related('names')
      # TODO ensure the sort is by the preferred name.
      # TODO sort - the following seems to break the response where there are multiple names.
      # queryset = queryset.order_by('names__item_name')
      # Default order by key until issue with name sort is fixed.
      queryset = queryset.order_by('location_key')
      return queryset

class LocationFeatureViewSet(viewsets.ModelViewSet):
    serializer_class = LocationFeatureSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
      'location_key': ['exact', 'isnull'],
    }

    def get_queryset(self):
      queryset = LocationFeature.objects.all()
      queryset = queryset.order_by('item_name')
      return queryset