# Generated by Django 3.2.7 on 2021-11-30 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='vaccine',
            field=models.CharField(choices=[('None', 'None'), ('CoronaVac (Sinovac)', 'CoronaVac (Sinovac)'), ('Gamaleya Sputnik V', 'Gamaleya Sputnik V'), ("Johnson and Johnson's Janssen", "Johnson and Johnson's Janssen"), ('Bharat BioTech', 'Bharat BioTech'), ('Moderna', 'Moderna'), ('Sinopharm', 'Sinopharm')], max_length=200, null=True),
        ),
    ]