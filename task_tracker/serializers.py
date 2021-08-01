from django.db.models import fields
from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    class Meta:
        model   = Task
        fields  = '__all__'