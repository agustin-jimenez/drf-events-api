import pytest
from django.db.models import QuerySet

from core.models import Event
from core.plotting import Plot


@pytest.mark.django_db()
class TestsPlot:
    """Test suite for Events model
    """

    def test_creating_a_plot_instance_successfully(self):
        """Test creating a plot instance without raising error
        """
        eventName = 'test'
        plot = Plot(eventName)
        assert isinstance(plot, Plot)
        assert plot.eventName == eventName
        assert isinstance(plot.qs, QuerySet)
