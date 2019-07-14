from django.contrib import admin

# Register your models here.
from .models import Course, CourseLesson, News, Profile, Lesson, FeedbackLesson, CourseLessonFeedback

admin.site.register(Course)
admin.site.register(CourseLesson)
admin.site.register(News)
admin.site.register(Profile)
admin.site.register(Lesson)
admin.site.register(FeedbackLesson)
admin.site.register(CourseLessonFeedback)