from django.db import models


class Event(models.Model):

    event = models.CharField(
        null=False,
        verbose_name='Event Name',
        max_length=255
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Date Created',
    )
    count = models.PositiveIntegerField(
        null=False,
        default=1,
        verbose_name='Count',
    )
