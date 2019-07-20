from django.db import models

class News(models.Model):
    title = models.CharField('Titel', max_length=200, blank=False)
    text = models.TextField('Nachricht', blank=False)
    pub_date = models.DateTimeField('Veröffentlichungsdatum')

    def __unicode__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Neuigkeit'
        verbose_name_plural = 'Neuigkeiten'

    def __str__(self):
        return self.title