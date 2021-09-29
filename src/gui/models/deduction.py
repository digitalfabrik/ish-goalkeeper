from django.db import models

class Deduction(models.Model):
    day = models.DateField('Tag (Datum)', auto_now=False, auto_now_add=False)
    school = models.TextField('Schule', max_length=500, blank=False)
    course = models.TextField('Klasse', max_length=500, blank=False)
    location = models.TextField('Ort', max_length=500, blank=False)
    rate = models.DecimalField('Stundensatz / Honorar', max_digits=40, decimal_places=2)

    def __str__(self):
        return self.school

    class Meta:
        verbose_name = 'Abrechnung'
        verbose_name_plural = 'Abrechnungen'