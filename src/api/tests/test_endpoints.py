import pytest
import os
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Event
from api.serializers import EventSerializer


# Define endpoint url globaly
os.environ.setdefault('BASE_URL', 'http://127.0.0.1:8000/api/')
BASE_URL = os.environ.get('BASE_URL')


@pytest.mark.django_db()
class TestsPublicEvents:

    EVENT_URL = ''.join((BASE_URL, 'event/'))

    @pytest.fixture()
    def client(self):
        """Initialize DRF APIClient"""
        yield APIClient()

    @pytest.fixture()
    def events(self):
        """Populate db with 4 events objects"""
        for _ in range(4):
            Event.objects.create(
                event='test',
                count=17
            )

    def test_creating_en_event(self, client):
        payload = {'event': 'some', 'count': 77}
        response = client.post(self.EVENT_URL, data=payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert Event.objects.filter(event=payload['event']).count()

    def test_listing_events(self, client, events):
        spectedResponse = EventSerializer(
            Event.objects.all(),
            many=True
        ).data
        actualResponse = client.get(self.EVENT_URL)
        assert actualResponse.status_code == status.HTTP_200_OK
        assert actualResponse.data == spectedResponse
