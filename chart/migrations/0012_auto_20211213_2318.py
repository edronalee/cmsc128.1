# Generated by Django 3.2.7 on 2021-12-13 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0011_auto_20211212_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='hospital',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='isolationfacility',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]