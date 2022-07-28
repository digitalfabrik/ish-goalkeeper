"""
Logos for log in screen
"""
from django.db import models
from filer.fields.file import FilerFileField


# pylint: disable=W5102
class Logo(models.Model):
    """
    Logos
    """
    title = models.CharField('Titel', max_length=200, blank=False)
    logo = FilerFileField(related_name='Logo',
                          null=True,
                          blank=True,
                          on_delete=models.CASCADE)
    main = models.BooleanField('Hauptlogo', blank=True)

    def __unicode__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Partnerlogo'
        verbose_name_plural = 'Partnerlogos'

    def __str__(self):
        return self.title
