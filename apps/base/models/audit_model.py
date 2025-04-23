from django.db import models
from apps.base.models.time_stamped_model import TimestampedModel
from apps.employees.models.employee import Employee

class AuditModel(TimestampedModel):
    executed_by = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_executed_by"
    )
