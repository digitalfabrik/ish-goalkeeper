from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .course import CourseLesson
from .lesson import FeedbackLesson

class CourseLessonFeedback(models.Model):
    course = models.ForeignKey(CourseLesson, on_delete=models.CASCADE, blank=False)
    feedbacklesson = models.ForeignKey(FeedbackLesson, on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField('Datum', blank=False)
    comment = models.TextField('Kommentar', max_length=1000, blank=True)
    gender_male = models.IntegerField('Männlich', validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    gender_female = models.IntegerField('Weiblich', validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    gender_other = models.IntegerField('Anderes Geschlecht', validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    positive = models.IntegerField('Grüne Bälle', validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    negative = models.IntegerField('Rote Bälle', validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

    def __str__(self):
        return self.course.course.title + " (" + (str(self.course.course.user)) + ") » " + self.course.lesson.title

    class Meta:
        verbose_name = 'Kursfeedback'
        verbose_name_plural = 'Kursfeedback'