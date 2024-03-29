"""
Models related to Lessons
"""
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from filer.fields.file import FilerFileField


class Lesson(MPTTModel):
    """
    Class for lessons, lessons are ordered in a tree
    """
    title = models.TextField("Titel", max_length=500, blank=False)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children',
                            db_index=True,
                            on_delete=models.CASCADE,
                            verbose_name="Übergeordnete Lektion")
    goal = models.TextField('Zielerklärung', blank=True)
    hints = models.TextField('Pädagogische Hinweise', blank=True)
    description = models.TextField('Beschreibung', blank=True)
    questions = models.TextField('Reflektionsfragen', blank=True)
    mandatory = models.BooleanField('Verpflichtend', blank=True)
    feedback_required = models.BooleanField('Feedback erforderlich',
                                            blank=True)

    def __str__(self):
        return ((str(self.parent) + " » " if self.parent is not None else "")
                + self.title)

    class Meta:
        """
        Meta information about Lessons
        """
        verbose_name = 'Lektion'
        verbose_name_plural = 'Lektionen'


class LessonMeta(models.Model):
    """
    Fields for meta information about lessons
    """
    description = models.TextField('Name', max_length=150)
    icon = FilerFileField(related_name='icon',
                          null=True,
                          blank=True,
                          on_delete=models.CASCADE,
                          verbose_name="Icon")

    def __str__(self):
        return self.description

    class Meta:
        """
        Meta information about LessonMeta
        """
        verbose_name = 'Lektionsmetafeld'
        verbose_name_plural = 'Lektionsmetafelder'


class LessonMetaData(models.Model):
    """
    Meta information about lessons
    """
    description = models.ForeignKey(LessonMeta, on_delete=models.CASCADE,
                                    verbose_name="Beschreibung")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               verbose_name="Lektion")
    value = models.TextField('Text', max_length=150)
    sort = models.IntegerField('Sortierung', default=-1)

    def __str__(self):
        return ('[ ' + self.lesson.title + ' ] '
                + self.description.description + ': ' + self.value)

    class Meta:
        """
        Meta information about LessonMetaData
        """
        verbose_name = 'Lektionsmetainformation'
        verbose_name_plural = 'Lektionsmetainformationen'
        ordering = ['sort']
        unique_together = (('description', 'lesson'),)


class Attachment(models.Model):
    """
    Attachments for lessons
    """
    title = models.TextField('Titel', max_length=150)
    attached_file = FilerFileField(related_name='attached_file',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE,
                                   verbose_name="Datei")
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               verbose_name="Lektion")

    class Meta:
        """
        Meta information about Attachment
        """
        verbose_name = 'Lektionsanhang'
        verbose_name_plural = 'Lektionsanhänge'

    def __str__(self):
        return self.title + " | " + self.lesson.title
