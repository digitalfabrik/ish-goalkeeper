"""
Define models for administration
"""
import csv
from django.contrib import admin
from django.http import HttpResponse
# pylint: disable=E0401
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Course, CourseUser, CourseLesson, News, Profile, Lesson
from .models import Feedback, LessonMeta, LessonMetaData, Attachment, Logo
from .models import KnowledgeArticle, KnowledgeAttachment


@admin.action(description='Datei als CSV exportieren')
# pylint: disable=W0613
def download_csv(modeladmin, request, queryset):
    """
    Export feedback into CSV and serve file as HTTP response
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=feedback.csv'
    writer = csv.writer(response, delimiter=';', quoting=csv.QUOTE_ALL)

    writer.writerow(["Lektion", "Kurs", "männlich", "weibich", "divers", "positiv",
                     "negativ", "Kommentar", "Kinderschutzrechtliche Anmerkung"])
    for feedback in queryset:
        writer.writerow([feedback.lesson, feedback.course, feedback.male, feedback.female,
                         feedback.other, feedback.positive, feedback.negative, feedback.comment,
                         feedback.childprotection])

    return response

# pylint: disable=R0903
class FeedbackAdmin(admin.ModelAdmin):
    """
    Add CSV download action for feedback
    """
    actions = [download_csv]

# pylint: disable=R0903
class LessonAdmin(SummernoteModelAdmin):
    """
    Rich Text Editor for Lessons
    """
    summernote_fields = ['description', 'questions', 'hints', 'goal']
    search_fields = ['title']

# pylint: disable=R0903
class CourseAdmin(admin.ModelAdmin):
    """
    Modify Course administration
    """
    search_fields = ['title']

# pylint: disable=R0903
class AttachmentAdmin(admin.ModelAdmin):
    """
    Modify Attachment administration
    """
    search_fields = ['title']

# pylint: disable=R0903
class NewsAdmin(SummernoteModelAdmin):
    """
    Rich Text editor for News
    """
    summernote_fields = 'text'

# pylint: disable=R0903
class KnowledgeArticleAdmin(SummernoteModelAdmin):
    """
    Rich Text editor for News
    """
    summernote_fields = 'content'
    search_fields = ['title']

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseLesson)
admin.site.register(News, NewsAdmin)
admin.site.register(Profile)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonMeta)
admin.site.register(LessonMetaData)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(CourseUser)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Logo)
admin.site.register(KnowledgeArticle, KnowledgeArticleAdmin)
admin.site.register(KnowledgeAttachment)
