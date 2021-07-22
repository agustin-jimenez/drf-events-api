import pytest

from rest_framework import status
from rest_framework.test import APIClient


class TestsPublicEvents:

    EVENT_CREATING_ENDPOINT = ''

    @pytest.fixture()
    def client(self):
        yield APIClient()
    '''
    def test_creating_en_event(self, client):
        payload = {'event': 'some', 'count': 77}
        response = client.post(self.EVENT_CREATING_ENDPOINT, data=payload)

        assert response.status_code == status.HTTP_201_CREATED
        # assert Event.objects.filter(name=payload['name']).count()

    '''
