# Generated by Django 3.2.7 on 2021-11-06 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0003_vitalsigns'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vitalsigns',
            new_name='Vitalsign',
        ),
    ]
