from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Lesson(MPTTModel):
    title = models.TextField(max_length=500, blank=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    description = models.TextField('Beschreibung', blank=True)
    questions = models.TextField('Fragen', blank=True)
    mandatory = models.BooleanField('Verpflichtend', blank=True)

    def __str__(self):
        return (str(self.parent) + " » " if self.parent is not None else "") + self.title

    class Meta:
        verbose_name = 'Lektion'
        verbose_name_plural = 'Lektionen'

class FeedbackLesson(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    feedback = models.BooleanField(name="Feedback erforderlich")

    def __str__(self):
        return (str(self.lesson.parent.title) + " » " if self.lesson.title is not None else "") + self.lesson.title

    class Meta:
        verbose_name = 'Lektion mit Feedback'
        verbose_name_plural = 'Lektionen mit Feedback'

class LessonMeta(models.Model):
    description = models.TextField('Name', max_length=150)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Lektionsmetafeld'
        verbose_name_plural = 'Lektionsmetafelder'

class LessonMetaData(models.Model):
    description = models.ForeignKey(LessonMeta, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    value = models.TextField('Datum', max_length=150)

    def __str__(self):
        return '[ ' + self.lesson.title + ' ] ' + self.description.description + ': ' + self.value

    class Meta:
        verbose_name = 'Lektionsmetainformation'
        verbose_name_plural = 'Lektionsmetainformationen'