from django.db import models
from django.contrib.auth.models import User
from .lesson import Lesson

class Course(models.Model):
    title = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=500, blank=True)
    start_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " (" + self.location + ") " + " - " + str(self.user)

class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title + " » " + self.lesson.title
