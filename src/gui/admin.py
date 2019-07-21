from django.contrib import admin

# Register your models here.
from .models import Course, CourseUsers, CourseLesson, News, Profile, Lesson, FeedbackLesson, CourseLessonFeedback, LessonMeta, LessonMetaData, File, Attachment

admin.site.register(Course)
admin.site.register(CourseLesson)
admin.site.register(News)
admin.site.register(Profile)
admin.site.register(Lesson)
admin.site.register(FeedbackLesson)
admin.site.register(LessonMeta)
admin.site.register(LessonMetaData)
admin.site.register(CourseLessonFeedback)
admin.site.register(CourseUsers)
admin.site.register(File)
admin.site.register(Attachment)