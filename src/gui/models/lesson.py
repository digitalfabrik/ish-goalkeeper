"""
Models related to Lessons
"""
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey  # pylint: disable=E0401
from filer.fields.file import FilerFileField  # pylint: disable=E0401


class Lesson(MPTTModel):  # pylint: disable=R0903
    """
    Class for lessons, lessons are ordered in a tree
    """
    title = models.TextField(max_length=500, blank=False)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children',
                            db_index=True,
                            on_delete=models.CASCADE)
    description = models.TextField('Beschreibung', blank=True)
    questions = models.TextField('Fragen', blank=True)
    mandatory = models.BooleanField('Verpflichtend', blank=True)
    feedback_required = models.BooleanField('Feedback erforderlich',
                                            blank=True)

    def __str__(self):
        return ((str(self.parent) + " » " if self.parent is not None else "")
                + self.title)

    # pylint: disable=R0903
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

    def __str__(self):
        return self.description

    # pylint: disable=R0903
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
    description = models.ForeignKey(LessonMeta, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    value = models.TextField('Datum', max_length=150)

    def __str__(self):
        # pylint: disable=E1101
        return ('[ ' + self.lesson.title + ' ] '
                + self.description.description + ': ' + self.value)

    # pylint: disable=R0903
    class Meta:
        """
        Meta information about LessonMetaData
        """
        verbose_name = 'Lektionsmetainformation'
        verbose_name_plural = 'Lektionsmetainformationen'


class Attachment(models.Model):
    """
    Attachments for lessons
    """
    description = models.TextField('Beschreibung', max_length=150)
    attached_file = FilerFileField(related_name='Anhang',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    # pylint: disable=R0903
    class Meta:
        """
        Meta information about Attachment
        """
        verbose_name = 'Anhang'
        verbose_name_plural = 'Anhänge'

    def __str__(self):
        # pylint: disable=E1101
        return self.file.description + " | " + self.lesson.title
