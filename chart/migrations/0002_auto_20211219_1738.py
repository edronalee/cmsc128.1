# Generated by Django 3.2.7 on 2021-12-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='antigenfile',
            field=models.FileField(blank=True, null=True, upload_to='pdf_uploads/', verbose_name='antigenfile'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rtpcrfile',
            field=models.FileField(blank=True, null=True, upload_to='pdf_uploads/', verbose_name='rtpcrfile'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='xrayfile',
            field=models.FileField(blank=True, null=True, upload_to='pdf_uploads/', verbose_name='xrayfile'),
        ),
    ]