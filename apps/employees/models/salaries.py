from django.db import models
from apps.base.models.time_stamped_model import TimestampedModel

class Salarie(TimestampedModel):
    employee = models.ForeignKey('employees.Employee', on_delete=models.PROTECT)
    amount = models.FloatField()
    currency = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()