# Generated by Django 3.2.7 on 2021-11-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0006_auto_20211116_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthtracker',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
