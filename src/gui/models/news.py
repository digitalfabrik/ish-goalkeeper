"""
News model
"""
from django.db import models
from django.contrib.auth.models import User, Group  # pylint: disable=E5142


class News(models.Model):  # pylint: disable=W5102
    """
    News model. Will be shown in News, except if menu_item is
    True. Then it will show up in the main menu.
    """
    title = models.CharField('Titel', max_length=200,
                             blank=False)
    text = models.TextField('Nachricht', blank=False)
    pub_date = models.DateTimeField('Veröffentlichungsdatum',
                                    auto_now_add=True)
    author = models.ForeignKey(User,
                               null=True, blank=True,
                               on_delete=models.SET_NULL,
                               verbose_name="Autor")
    menu_item = models.BooleanField(null=True, blank=True,
                                    verbose_name="Hauptmenü")
    groups = models.ManyToManyField(Group, blank=True)

    def __unicode__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Neuigkeit'
        verbose_name_plural = 'Neuigkeiten'

    def __str__(self):
        return self.title
