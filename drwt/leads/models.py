"""Leads models settings."""
from django.db import models


class Lead(models.Model):
    """Lead model."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
