from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, Http404
from .lesson import Lesson


class Course(models.Model):
    title = models.TextField('Kurstitel', max_length=500, blank=False)
    location = models.TextField('Ort', max_length=500, blank=False)
    active = models.BooleanField('Aktiv', blank=True)
    dates = models.TextField('Kurszeit', max_length=500, blank=True)

    def __str__(self):
        return self.title + " (" + self.location + ") "

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


class CourseUser(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.course.title + " - " + str(self.user)

    class Meta:
        verbose_name = 'Coach-Zuordnung'
        verbose_name_plural = 'Coach-Zuordnungen'


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
