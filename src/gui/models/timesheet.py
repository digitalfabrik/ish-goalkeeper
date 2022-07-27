"""
All models related to the time sheet functionality
"""

from django.db import models

from django.contrib.auth.models import User  # pylint: disable=E5142
from .course import Course


class HourlyRate(models.Model):
    """
    The hourly rates that are possible
    """
    rate = models.IntegerField('Stundensatz', blank=False)

    class Meta:
        verbose_name = 'Stundensatz'
        verbose_name_plural = 'Stundensätze'

    def __str__(self):
        return str(self.rate)

class TimeSheet(models.Model):
    """
    Spent time on courses per user associated with an hourly rate
    """
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name="Kurs")
    instructor = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   verbose_name="Kursleiter*in")
    hours = models.FloatField('Stunden')
    date = models.DateField('Tag')
    rate = models.ForeignKey(HourlyRate,
                             on_delete=models.CASCADE,
                             verbose_name="Stundensatz")

    class Meta:
        verbose_name = 'Stundenerfassung'
        verbose_name_plural = 'Stundenerfassung'

    def __str__(self):
        return f"{self.instructor}, {self.course}, {self.date}: {self.hours} × {self.rate} EUR"
