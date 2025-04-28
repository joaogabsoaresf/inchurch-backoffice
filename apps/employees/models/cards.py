from django.db import models

from apps.base.models.time_stamped_model import TimestampedModel


class Card(TimestampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    request_type = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.status}"
