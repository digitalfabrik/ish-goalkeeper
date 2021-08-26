"""
Models related to collecting feedback
"""
# pylint: disable=E0401
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
from .lesson import Lesson
from .course import Course


class Feedback(models.Model):  # pylint: disable=R0903
    """
    Class for collecting feedback
    """
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               blank=False,
                               verbose_name="Kurs")
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               blank=False,
                               verbose_name="Lektion")
    date = models.DateTimeField('Datum', blank=False, default=now)
    comment = models.TextField('Kommentar des Coaches', max_length=1000, blank=True)
    quote_child = models.TextField('Zitat eines Kindes', max_length=1000, blank=True)
    childprotection = models.TextField('Kinderschutzrelevante Information',
                                       max_length=1000, blank=True)
    male = models.IntegerField(
        'Männlich',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    female = models.IntegerField(
        'Weiblich',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    other = models.IntegerField(
        'Anderes Geschlecht',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    positive = models.IntegerField(
        'Grüne Bälle',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    negative = models.IntegerField(
        'Rote Bälle',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    start_blue = models.IntegerField(
        'Blaue Bälle zu Beginn',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    start_yellow = models.IntegerField(
        'Gelbe Bälle zu Beginn',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    start_green = models.IntegerField(
        'Grüne Bälle zu Beginn',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    start_red = models.IntegerField(
        'Rote Bälle zu Beginn',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    end_blue = models.IntegerField(
        'Blaue Bälle zum Ende',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    end_yellow = models.IntegerField(
        'Gelbe Bälle zum Ende',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    end_green = models.IntegerField(
        'Grüne Bälle zum Ende',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)
    end_red = models.IntegerField(
        'Rote Bälle zum Ende',
        validators=[MaxValueValidator(99), MinValueValidator(0)],
        default=0)

    def __str__(self):
        # pylint: disable=E1101
        return (self.course.title + " ("
                + ") » "
                + self.lesson.title)

    # pylint: disable=R0903
    class Meta:
        """
        Meta information about Feedback
        """
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
        unique_together = (('course', 'lesson'),)
