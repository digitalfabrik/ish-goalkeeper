from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .course import CourseLesson
from .lesson import FeedbackLesson

class CourseLessonFeedback(models.Model):
    course = models.ForeignKey(CourseLesson, on_delete=models.CASCADE)
    feedbacklesson = models.ForeignKey(FeedbackLesson, on_delete=models.CASCADE)
    date = models.DateTimeField('feedback date')
    positive = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    negative = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])

    def __str__(self):
        return self.course.course.title + " (" + (str(self.course.course.user)) + ") » " + self.course.lesson.title
