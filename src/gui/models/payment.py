from django.db import models
from django.contrib.auth.models import Course

class Payment(models.Model):
    """
    Model for Payment
    """
    day=models.DateField()
    courses=models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=False, verbose_name="Kurs"
    )
    time=models.TimeField()