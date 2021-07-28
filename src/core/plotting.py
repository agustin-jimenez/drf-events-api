import plotly.express as px
from pandas import DataFrame

from core.models import Event


class Plot:

    def __init__(self, eventName):
        self.eventName = eventName
        self.qs = Event.objects.filter(event=eventName)
        self.create_df_from_queryset()

    def create_df_from_queryset(self):
        self.df = DataFrame(list(self.qs.values('date', 'count')))

    def get_histogram(self):
        fig = px.histogram(self.df, x='date')
        return fig.to_image(format="png")


