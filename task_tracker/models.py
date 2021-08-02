from django.db import models
from datetime import date

class Task (models.Model):
    text        = models.TextField()
    day         = models.DateField(default=date.today)
    reminder    = models.BooleanField(default=False)