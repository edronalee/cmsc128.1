# Generated by Django 3.2.7 on 2021-10-25 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('barangay', models.CharField(choices=[('Alabang', 'Alabang'), ('Ayala-Alabang', 'Ayala-Alabang'), ('Bayanan', 'Bayanan'), ('Buli', 'Buli'), ('Cupang', 'Cupang'), ('Poblacion', 'Poblacion'), ('Putatan', 'Putatan'), ('Sucat', 'Sucat'), ('Tunasan', 'Tunasan')], max_length=200, null=True)),
                ('city', models.CharField(choices=[('Muntinlupa', 'Muntinlupa')], max_length=200, null=True)),
                ('numchild', models.CharField(blank=True, max_length=200, null=True)),
                ('namechild', models.CharField(blank=True, max_length=200, null=True)),
                ('contactnumber', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('vaccine', models.CharField(blank=True, max_length=200, null=True)),
                ('firstdose', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True)),
                ('seconddose', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True)),
                ('fdosedate', models.DateField(blank=True, null=True)),
                ('sdosedate', models.DateField(blank=True, null=True)),
                ('telemedicine', models.CharField(choices=[('TelAventusMD', 'TelAventusMD'), ('SeeYouDoc', 'SeeYouDoc'), ('MedCheck', 'MedCheck'), ('TeliMed', 'TeliMed'), ('KonsultaMD', 'KonsultaMD'), ('CloudPx', 'CloudPx'), ('HealthNow', 'HealthNow')], max_length=200, null=True)),
                ('antigenresult', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=200, null=True)),
                ('antigendate', models.DateField(null=True)),
                ('rtpcrresult', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=200, null=True)),
                ('rtpcrdate', models.DateField(null=True)),
                ('xray', models.CharField(choices=[('Chest Xray', 'Chest Xray'), ('Film Array', 'Film Array')], max_length=200, null=True)),
                ('xraydate', models.DateField(null=True)),
                ('status', models.CharField(choices=[('For Monitoring', 'For Monitoring'), ('For Referral', 'For Referral'), ('For Transfer', 'For Transfer')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(null=True)),
                ('lastdate', models.DateField(null=True)),
                ('question3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True)),
                ('question4', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True)),
                ('question5', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chart.patient')),
            ],
        ),
    ]
