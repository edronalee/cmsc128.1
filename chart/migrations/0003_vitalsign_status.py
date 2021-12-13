# Generated by Django 3.2.7 on 2021-12-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_alter_patient_vaccine'),
    ]

    operations = [
        migrations.AddField(
            model_name='vitalsign',
            name='status',
            field=models.CharField(choices=[('For Monitoring', 'For Monitoring'), ('For Referral', 'For Referral'), ('For Transfer', 'For Transfer')], max_length=200, null=True),
        ),
    ]
