# Generated by Django 3.2.7 on 2021-10-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0005_auto_20211023_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
