# Generated by Django 2.2.1 on 2019-09-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0011_auto_20190821_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='timeframe',
            field=models.TextField(blank=True, verbose_name='Umfang'),
        ),
    ]