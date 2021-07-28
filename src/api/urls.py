from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import *


public = DefaultRouter()

public.register("event", EventsListCreateViewSet, basename='events')


urlpatterns = [
    path("", include(public.urls)),
    path("plot/<str:event>/", plot_events_from_event_name, name='plot'),
]
