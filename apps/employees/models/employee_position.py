from django.db import models

from apps.base.models.time_stamped_model import TimestampedModel


class EmployeePosition(TimestampedModel):
    employee = models.ForeignKey("employees.Employee", on_delete=models.PROTECT)  # noqa
    position = models.ForeignKey("employees.Position", on_delete=models.PROTECT)  # noqa
    start_date = models.DateField()
    end_date = models.DateField()
