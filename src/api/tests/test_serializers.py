import pytest
import json
from datetime import date

from core.models import Event
from api.serializers import EventSerializer


@pytest.mark.django_db()
class TestsEventSerialization:

    @pytest.fixture()
    def event(self):
        instance = Event.objects.create(
            event='some',
            count=2,
        )
        yield instance

    def test_serializing_an_event_object(self, event):
        spected = {
            'date': event.date.isoformat(),
            'event': event.event,
            'count': event.count,
        }
        actual = EventSerializer(event, many=False).data
        assert actual == spected
