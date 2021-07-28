from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

import django_filters.rest_framework as filters
from django.http import HttpResponse

from core.models import Event
from core.plotting import Plot
from api.serializers import EventSerializer


class EventsFilter(filters.FilterSet):

    """Provide queryparams for Events endpoint"""

    start_date = filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='date', lookup_expr='lte')
    event_name = filters.CharFilter(field_name='event', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['start_date', 'end_date', 'event_name']


class EventsListCreateViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):

    "Define Events endpoint behavior"

    serializer_class = EventSerializer
    permission_classes = (AllowAny,)
    filterset_class = EventsFilter
    queryset = Event.objects.all()


@api_view()
def plot_events_from_event_name(request, event):
    return HttpResponse(
            Plot(event).get_histogram(),
            content_type="image/png"
          )
