from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from core.models import Event
from api.serializers import EventSerializer


class EventsListCreateViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)
    queryset = Event.objects.all()
