from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


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
        validators=[
            MinValueValidator(1),
        ],
    )

    def save(self, *args, **kwargs):
        if self.count == 0:
            raise ValidationError('Count minimum value is 1')
        super(Event, self).save(*args, **kwargs)
