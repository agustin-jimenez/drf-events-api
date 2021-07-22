import pytest
from datetime import date
from django.core.exceptions import ValidationError

from core.models import Event


@pytest.mark.django_db()
class TestsEvents:
    """Test suite for Events model
    """

    def test_creating_event_successfully(self):
        """Test creating an event without raising error
        """
        e = Event.objects.create(
            event='some',
            count=2,
        )
        assert Event.objects.count()
        assert isinstance(e.event, str)
        assert isinstance(e.date, date)
        assert e.count

    def test_creating_an_event_with_zero_count_raises_error(self):
        """Test creating an event with 0 count raises error
        """
        with pytest.raises(ValidationError):
            e = Event.objects.create(
                event='some',
                count=0,
            )
