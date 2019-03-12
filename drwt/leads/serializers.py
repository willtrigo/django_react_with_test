"""Serializer lead settings."""
from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    """Serializer lead."""

    class Meta:
        """Settings lead."""

        model = Lead
        fields = ('id', 'name', 'email', 'message')
        # fields = '__all__'
