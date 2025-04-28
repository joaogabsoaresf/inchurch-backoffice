from django.db import models


class ActiveQuerySet(models.QuerySet):
    def delete(self):
        self.update(is_active=False)

    def active(self):
        return self.filter(is_active=True).distinct()


class ActiveManager(models.Manager):
    def get_queryset(self):
        return ActiveQuerySet(self.model, using=self._db)

    def all_with_inactive(self):
        return super().get_queryset()

    def active(self):
        return self.get_queryset().active()
