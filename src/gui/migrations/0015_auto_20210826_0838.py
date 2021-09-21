# Generated by Django 3.2.6 on 2021-08-26 08:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0014_feedback_childprotection'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='end_blue',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], verbose_name='Blaue Bälle zum Ende'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='end_green',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], verbose_name='Grüne Bälle zum Ende'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='end_red',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], verbose_name='Rote Bälle zum Ende'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='end_yellow',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], verbose_name='Gelbe Bälle zum Ende'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='start_blue',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], verbose_name='Blaue Bälle zu Beginn'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='start_green',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], verbose_name='Grüne Bälle zu Beginn'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='start_red',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], verbose_name='Rote Bälle zu Beginn'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='start_yellow',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], verbose_name='Gelbe Bälle zu Beginn'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='questions',
            field=models.TextField(blank=True, verbose_name='Reflektionsfragen'),
        ),
    ]