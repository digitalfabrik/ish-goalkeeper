# Generated by Django 2.2.1 on 2020-03-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0013_auto_20200310_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='childprotection',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Kinderschutzrelevante Information'),
        ),
    ]