# Generated by Django 3.2.14 on 2022-07-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0023_auto_20220727_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]