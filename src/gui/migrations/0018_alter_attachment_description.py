# Generated by Django 3.2.6 on 2021-09-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0017_auto_20210921_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='description',
            field=models.TextField(max_length=150, verbose_name='Titel'),
        ),
    ]
