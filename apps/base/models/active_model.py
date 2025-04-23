from django.db import models

from apps.base.querysets import ActiveManager

class ActiveModel(models.Model):
    """ Use `is_active` state of model instead of delete it
    """
    is_active = models.BooleanField(default=True, editable=False)
    class Meta:
        abstract = True

    def delete(self):
        self.is_active = False
        self.save()

    objects = ActiveManager()
