from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('Biographie', max_length=500, blank=True)
    location = models.CharField('Wohnort', max_length=30, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profile'