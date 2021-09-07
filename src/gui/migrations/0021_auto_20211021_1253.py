# Generated by Django 3.2.6 on 2021-10-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0020_auto_20211021_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='goal',
            field=models.TextField(blank=True, max_length=500, verbose_name='Zielerklärung'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='hints',
            field=models.TextField(blank=True, max_length=500, verbose_name='Pädagogische Hinweise'),
        ),
    ]
