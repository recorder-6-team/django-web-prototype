import django_filters.rest_framework
from .serializers import LocationSerializer
from rest_framework import viewsets
from rest_framework import permissions
from apps.locations.models import Location, LocationName

class LocationViewSet(viewsets.ModelViewSet):
    # Prefetch related location names so they can be included in response.
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
      'parent_key': ['exact', 'isnull'],
    }

    def get_queryset(self):
      queryset = Location.objects.all()
      # Ensure location names available without additional query.
      queryset = queryset.prefetch_related('names')
      # Sort by name.
      # TODO ensure the sort is by the preferred name.
      queryset = queryset.order_by('names__item_name')
      return queryset