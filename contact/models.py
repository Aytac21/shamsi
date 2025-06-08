from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"

    def __str__(self):
        return f"{self.name} - {self.subject}"
