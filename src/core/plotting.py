import plotly.express as px
from base64 import b64encode

from core.models import Event


class Plot:

    def __init__(self, eventName):
        self.eventName = eventName
        self.qs = Event.objects.filter(event=eventName)

    def encoding(self, bStr):
        return "data:image/png;base64," + b64encode(bStr).decode()

    def get_histogram(self):
        fig = px.histogram()
        imgBytes = fig.to_image(format="png")
        return self.encoding(imgBytes)


