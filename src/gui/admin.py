from django.contrib import admin

# Register your models here.
from .models import Course, CourseUser, CourseLesson, News, Profile, Lesson, Feedback, LessonMeta, LessonMetaData, Attachment

admin.site.register(Course)
admin.site.register(CourseLesson)
admin.site.register(News)
admin.site.register(Profile)
admin.site.register(Lesson)
admin.site.register(LessonMeta)
admin.site.register(LessonMetaData)
admin.site.register(Feedback)
admin.site.register(CourseUser)
admin.site.register(Attachment)
