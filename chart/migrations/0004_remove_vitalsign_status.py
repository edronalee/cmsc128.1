# Generated by Django 3.2.7 on 2021-12-01 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0003_vitalsign_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vitalsign',
            name='status',
        ),
    ]