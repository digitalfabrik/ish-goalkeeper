from django.db import models
from django.contrib.auth.models import User
from .lesson import Lesson
import datetime

class Course(models.Model):
    title = models.TextField('Kurstitel', max_length=500, blank=False)
    location = models.TextField('Ort', max_length=500, blank=False)
    active = models.BooleanField('Aktiv', blank=True)
    dates = models.TextField('Kurszeit', max_length=500, blank=True)

    def __str__(self):
        return self.title + " (" + self.location + ") " + " - " + str(self.user)

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurse'

class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title + " » " + self.lesson.title

    class Meta:
        verbose_name = 'Kurslektion'
        verbose_name_plural = 'Kurslektionen'

class CourseUsers(models.Model):
    user = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.course.title + " &mdash; " + self.user

    class Meta:
        verbose_name = 'Kurs-Benutzer-Zuteilung'
        verbose_name_plural = 'Kurs-Benutzer-Zuteilungen'