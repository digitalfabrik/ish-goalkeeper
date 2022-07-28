"""
Define models for administration
"""
import csv
from datetime import datetime
from django.contrib import admin
from django.http import HttpResponse
from django_summernote.admin import SummernoteModelAdmin

from rangefilter.filters import DateRangeFilter

# Register your models here.
from .models import Course, CourseUser, CourseLesson, News, Profile, Lesson
from .models import Feedback, LessonMeta, LessonMetaData, Attachment, Logo
from .models import KnowledgeArticle, KnowledgeAttachment
from .models import HourlyRate, TimeSheet

def feedback_to_csv(queryset, writer):
    """
    Convert feedback to csv
    """
    writer.writerow(["Lektion", "Kurs", "männlich", "weibich", "divers", "positiv",
                     "negativ", "Kommentar", "Kinderschutzrechtliche Anmerkung"])
    for feedback in queryset:
        writer.writerow([feedback.lesson, feedback.course, feedback.male, feedback.female,
                         feedback.other, feedback.positive, feedback.negative, feedback.comment,
                         feedback.childprotection])

def timesheet_to_csv(queryset, writer):
    """
    Convert timesheet data to CSV
    """
    writer.writerow(["Kursleiter*in", "Kurs", "Datum", "Stunden", "Stundensatz"])
    for row in queryset:
        writer.writerow([row.instructor, row.course, row.date, row.hours, row.rate])

@admin.action(description='Datei als CSV exportieren')
# pylint: disable=W0613
def download_csv(modeladmin, request, queryset):
    """
    Export feedback into CSV and serve file as HTTP response
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data.csv'
    writer = csv.writer(response, delimiter=';', quoting=csv.QUOTE_ALL)

    if str(modeladmin) == "gui.TimeSheetAdmin":
        timesheet_to_csv(queryset, writer)
    elif str(modeladmin) == "gui.FeedbackAdmin":
        feedback_to_csv(queryset, writer)
    return response

class TimeSheetAdmin(admin.ModelAdmin):
    """
    Add search filters and CSV export to Time Sheet
    """
    list_filter = (
        ('date', DateRangeFilter),
        'instructor',
    )
    actions = [download_csv]

    def get_rangefilter_date_default(self, request):  # pylint: disable=R0201
        """
        register filters for date
        """
        return (datetime.today(), datetime.today())

class FeedbackAdmin(admin.ModelAdmin):
    """
    Add CSV download action for feedback
    """
    actions = [download_csv]

class LessonAdmin(SummernoteModelAdmin):
    """
    Rich Text Editor for Lessons
    """
    summernote_fields = ['description', 'questions', 'hints', 'goal']
    search_fields = ['title']

class CourseAdmin(admin.ModelAdmin):
    """
    Modify Course administration
    """
    search_fields = ['title']

class AttachmentAdmin(admin.ModelAdmin):
    """
    Modify Attachment administration
    """
    search_fields = ['title']

class NewsAdmin(SummernoteModelAdmin):
    """
    Rich Text editor for News
    """
    summernote_fields = 'text'

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
admin.site.register(HourlyRate)
admin.site.register(TimeSheet, TimeSheetAdmin)
