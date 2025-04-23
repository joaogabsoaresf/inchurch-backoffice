from django.db import models
from apps.base.models.time_stamped_model import TimestampedModel

class Position(TimestampedModel):
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.department}-{self.title}"
