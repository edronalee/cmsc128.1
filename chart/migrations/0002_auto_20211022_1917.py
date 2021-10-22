# Generated by Django 3.2.7 on 2021-10-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='fdosedate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='firstdose',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='seconddose',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='namechild',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='numchild',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='vaccine',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
