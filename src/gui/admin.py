"""
Define models for administration
"""
from django.contrib import admin
# pylint: disable=E0401
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Course, CourseUser, CourseLesson, News, Profile, Lesson
from .models import Feedback, LessonMeta, LessonMetaData, Attachment, Logo


# pylint: disable=R0903
class LessonAdmin(SummernoteModelAdmin):
    """
    Rich Text Editor for Lessons
    """
    summernote_fields = ['description', 'questions']
    search_fields = ['title']


# pylint: disable=R0903
class NewsAdmin(SummernoteModelAdmin):
    """
    Rich Text editor for News
    """
    summernote_fields = 'text'

class CourseAdmin(admin.ModelAdmin):
    """
    Modify Course administration
    """
    search_fields = ['title']

class AttachmentAdmin(admin.ModelAdmin):
    """
    Modify Attachment administration
    """
    search_fields = ['description']


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseLesson)
admin.site.register(News, NewsAdmin)
admin.site.register(Profile)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonMeta)
admin.site.register(LessonMetaData)
admin.site.register(Feedback)
admin.site.register(CourseUser)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Logo)
