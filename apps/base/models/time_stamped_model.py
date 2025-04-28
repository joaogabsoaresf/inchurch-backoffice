from django.db import models
from django.utils import timezone

from apps.base.models.active_model import ActiveModel


class TimestampedModel(ActiveModel):
    @staticmethod
    def current_time_minus_3_hours():
        return timezone.now() - timezone.timedelta(hours=3)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
