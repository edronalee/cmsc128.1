# Generated by Django 3.2.7 on 2021-12-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0012_auto_20211209_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='has_cancer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=200, verbose_name='Cancer'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_diabetes',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=200, verbose_name='Diabetes'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_gastro',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=200, verbose_name='Gastrointestinal Diseases'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_genito',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=200, verbose_name='Genitourinary Diseases'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_heart_disease',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=200, verbose_name='Heart Diseases'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_hypertension',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=200, verbose_name='Hypertension'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_lung_disease',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=200, verbose_name='Lung Diseases'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_neuro',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=200, verbose_name='Neurological Diseases'),
        ),
    ]
