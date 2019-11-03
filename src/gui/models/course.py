from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, Http404
from .lesson import Lesson


class Course(models.Model):
    title = models.TextField('Kurstitel', max_length=500, blank=False)
    location = models.TextField('Ort', max_length=500, blank=False)
    active = models.BooleanField('Aktiv', blank=True)
    timeframe = models.TextField('Umfang', blank=True)
    dates = models.TextField('Kurszeit', max_length=500, blank=True)

    def __str__(self):
        return self.title + " (" + self.location + ") "

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurse'


class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name="Kurs")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               verbose_name="Lektion")

    def __str__(self):
        return self.course.title + " » " + self.lesson.title

    class Meta:
        verbose_name = 'Zuordnung Kurs-Lektion'
        verbose_name_plural = 'Zuordnungen Kurs-Lektion'


class CourseUser(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False,
                               verbose_name="Kurs")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False,
                             verbose_name="Benutzer")

    def __str__(self):
        return self.course.title + " - " + str(self.user)

    class Meta:
        verbose_name = 'Zuordnung Kurs-Benutzer'
        verbose_name_plural = 'Zuordnungen Kurs-Benutzer'


def access_course(function):
    def user_can_access(request, **kwargs):
        if 'course_id' not in kwargs:
            return function(request, **kwargs)
        course_id = int(kwargs['course_id'])
        courses = Course.objects.filter(id=course_id)
        if not courses:
            raise Http404
        course = courses[0]
        try:
            CourseUser.objects.get(user=request.user, course=course)
        except CourseUser.DoesNotExist:
            return HttpResponseForbidden("Forbidden")
        else:
            return function(request, **kwargs)
    return user_can_access
