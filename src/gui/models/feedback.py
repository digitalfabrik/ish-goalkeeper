"""
Models related to collecting feedback
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .lesson import Lesson
from .course import CourseLesson


class Feedback(models.Model):
    """
    Class for collecting feedback
    """
    course = models.ForeignKey(CourseLesson,
                               on_delete=models.CASCADE,
                               blank=False)
    feedbacklesson = models.ForeignKey(Lesson,
                                       on_delete=models.CASCADE,
                                       blank=False)
    date = models.DateTimeField('Datum', blank=False)
    comment = models.TextField('Kommentar', max_length=1000, blank=True)
    gender_male = models.IntegerField('Männlich', validators=[
        MaxValueValidator(100),
        MinValueValidator(0)])
    gender_female = models.IntegerField('Weiblich', validators=[
        MaxValueValidator(100),
        MinValueValidator(0)])
    gender_other = models.IntegerField('Anderes Geschlecht', validators=[
        MaxValueValidator(100),
        MinValueValidator(0)])
    positive = models.IntegerField('Grüne Bälle', validators=[
        MaxValueValidator(100),
        MinValueValidator(0)])
    negative = models.IntegerField('Rote Bälle', validators=[
        MaxValueValidator(100),
        MinValueValidator(0)])

    def __str__(self):
        # pylint: disable=E1101
        return (self.course.course.title + " ("
                + (str(self.course.course.user)) + ") » "
                + self.course.lesson.title)

    # pylint: disable=R0903
    class Meta:
        """
        Meta information about Feedback
        """
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
