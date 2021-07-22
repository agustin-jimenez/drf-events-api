from rest_framework import serializers

from core.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['date', 'event', 'count']
