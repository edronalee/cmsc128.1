# Generated by Django 3.2.7 on 2021-10-22 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0003_auto_20211022_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='healthhistory',
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chart.patient'),
        ),
    ]
