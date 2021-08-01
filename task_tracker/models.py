from django.db import models
from datetime import datetime

class Task (models.Model):
    text        = models.TextField()
    day         = models.DateTimeField(default=datetime.now())
    reminder    = models.BooleanField(default=False)