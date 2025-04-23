from django.db import models
from apps.employees.choices import RoleChoices, TeamChoices
from django.contrib.postgres.fields import ArrayField
from apps.base.models.time_stamped_model import TimestampedModel

class Employee(TimestampedModel):
    google_user_id = models.CharField(max_length=100, unique=True, db_index=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=RoleChoices.choices, null=True, default=RoleChoices.BASIC)
    team = ArrayField(
            models.CharField(max_length=50, choices=TeamChoices.choices),
            default=list,
            blank=True,
        )
    is_onboarded = models.BooleanField(default=False, null=False)
    
    document_number = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)

    phone = models.CharField(max_length=20, null=True)
    address = models.JSONField(default=dict, null=True)

    hire_date = models.DateField(null=True)
    firement_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.role}: {self.full_name}"
    
    
    def save(self, *args, **kwargs):
        if self.team is None or not isinstance(self.team, list):
            self.team = [TeamChoices.OTHER]

        super().save(*args, **kwargs)
