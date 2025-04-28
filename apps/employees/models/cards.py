from django.db import models


class Card(models.Model):
    card_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    request_type = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.status}"
