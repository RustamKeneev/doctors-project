# Generated by Django 3.1.4 on 2021-01-25 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название специалиста')),
            ],
            options={
                'verbose_name': 'Профессия специалиста',
                'verbose_name_plural': 'Профессии специалистов',
            },
        ),
        migrations.CreateModel(
            name='MedicalStaffPositions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Должность специалиста')),
                ('medical_staff_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Количество объявлений')),
            ],
            options={
                'verbose_name': 'Должность специалиста',
                'verbose_name_plural': 'Должности специалистов',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorFullName', models.CharField(max_length=256, verbose_name='Фамилия Имя Отчество')),
                ('firstName', models.CharField(max_length=128, verbose_name='Имя')),
                ('secondName', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('lastName', models.CharField(max_length=128, verbose_name='Отчество ')),
                ('doctorPhoneNumber', models.PositiveIntegerField(verbose_name='Номер телефона')),
                ('doctorEducation', models.TextField(verbose_name='Образование')),
                ('doctorImage', models.ImageField(null=True, upload_to='doctorsImage/')),
                ('doctorInfo', models.TextField(verbose_name='Информация о специалиста')),
                ('doctorStatus', models.CharField(max_length=128, verbose_name='Статус специалиста')),
                ('doctorWorkLocation', models.CharField(max_length=512, verbose_name='Адресс работы специалиста')),
                ('doctorType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctors.doctortype', verbose_name='Профессия специалиста')),
                ('medical_staff_positions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctors.medicalstaffpositions', verbose_name='Должность')),
                ('user_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Специалиста',
                'verbose_name_plural': 'Специалисты',
            },
        ),
    ]
