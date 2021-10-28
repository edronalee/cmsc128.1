# Generated by Django 3.2.7 on 2021-10-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now_add=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('firstname', models.CharField(max_length=200, null=True, verbose_name='first name')),
                ('lastname', models.CharField(max_length=200, null=True, verbose_name='last name')),
                ('address', models.CharField(max_length=200, null=True)),
                ('barangay', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('birthdate', models.DateField(blank=True, verbose_name='birth date')),
                ('age', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('licensenumber', models.CharField(max_length=200, null=True, verbose_name='license number')),
                ('licenseexpiry', models.DateField(verbose_name='license expiry')),
                ('licensepic', models.ImageField(blank=True, null=True, upload_to='', verbose_name='license picture')),
                ('contactnumber', models.CharField(max_length=200, null=True, verbose_name='contact number')),
                ('specialization', models.CharField(choices=[('General Practitioner', 'General Practitioner'), ('Family Medicine', 'Family Medicine')], max_length=200, null=True)),
                ('schedule', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LGUAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now_add=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('firstname', models.CharField(max_length=200, null=True, verbose_name='first name')),
                ('lastname', models.CharField(max_length=200, null=True, verbose_name='last name')),
                ('address', models.CharField(max_length=200, null=True)),
                ('barangay', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('birthdate', models.DateField(verbose_name='birth date')),
                ('age', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('employeenumber', models.CharField(max_length=200, null=True, verbose_name='employee number')),
                ('contactnumber', models.CharField(max_length=200, null=True, verbose_name='contact number')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
