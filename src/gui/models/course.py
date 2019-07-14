from django.db import models
from django.contrib.auth.models import User
from .lesson import Lesson
import datetime

class Course(models.Model):
    title = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=500, blank=True)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dates = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title + " (" + self.location + ") " + " - " + str(self.user)

class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title + " » " + self.lesson.title
