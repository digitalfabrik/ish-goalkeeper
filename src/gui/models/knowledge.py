"""
Models related to Knowledge (base)
"""
from django.db import models  # pylint: disable=E0401
from mptt.models import MPTTModel, TreeForeignKey  # pylint: disable=E0401
from filer.fields.file import FilerFileField  # pylint: disable=E0401


class KnowledgeArticle(MPTTModel):  # pylint: disable=R0903
    """
    Class for lessons, lessons are ordered in a tree
    """
    title = models.CharField("Titel", max_length=500, blank=False)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children',
                            db_index=True,
                            on_delete=models.CASCADE,
                            verbose_name="Übergeordneter Artikel")
    content = models.TextField('Inhalt', blank=True)

    def __str__(self):
        return ((str(self.parent) + " » " if self.parent is not None else "")
                + self.title)

    # pylint: disable=R0903
    class Meta:
        """
        Meta information about Lessons
        """
        verbose_name = 'Wissen-Artikel'
        verbose_name_plural = 'Wissen-Artikel'


class KnowledgeAttachment(models.Model):  # pylint: disable=R0903
    """
    Attachments for lessons
    """
    title = models.CharField('Titel', max_length=150)
    attached_file = FilerFileField(related_name='knowledge_file',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE,
                                   verbose_name="Datei")
    knowledge_article = models.ForeignKey(KnowledgeArticle,
                                          on_delete=models.CASCADE,
                                          verbose_name="Wissen-Artikel",
                                          related_name='attachments')

    # pylint: disable=R0903
    class Meta:
        """
        Meta information about Attachment
        """
        verbose_name = 'Wissens-Artikel-Anhang'
        verbose_name_plural = 'Wissens-Artikel-Anhänge'

    def __str__(self):
        # pylint: disable=E1101
        return self.title + " | " + self.knowledge_article.title
