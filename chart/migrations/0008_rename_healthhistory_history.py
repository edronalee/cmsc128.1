# Generated by Django 3.2.7 on 2021-10-24 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0007_alter_patient_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HealthHistory',
            new_name='History',
        ),
    ]
