import pytest
from datetime import date

from core.models import Event


@pytest.mark.django_db()
class TestsEvents:
    """Test suite for Events model
    """
    def test_creating_event_successfully(self):
        """Test creating an event without raising error
        """
        e = Event.objects.create(
            name='some',
            count=2,
        )
        assert Event.objects.count()
        assert isinstance(e.name, str)
        assert isinstance(e.date, date)
        assert e.count
