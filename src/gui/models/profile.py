"""
Add profile information for users
"""

from django.db import models
from django.contrib.auth.models import User  # pylint: disable=E5142

class Profile(models.Model):
    """
    Profile class with information that extends the user class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField('Biographie', max_length=500, blank=True)
    location = models.CharField('Wohnort', max_length=30, blank=True)
    contract_start_date = models.DateField('Startdatum Übungsleitervertrag', blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(blank=True, upload_to="profile/", height_field=None, width_field=None)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profile'
