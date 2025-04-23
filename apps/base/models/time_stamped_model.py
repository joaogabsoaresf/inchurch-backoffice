from django.db import models
from apps.base.models.active_model import ActiveModel


class TimestampedModel(ActiveModel):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
