"""Выф."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Выф."""

    class Meta:
        """Выф."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
