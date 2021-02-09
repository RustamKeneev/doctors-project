from django.conf import settings
from django.db import models


class Doctors(models.Model):
    class Meta:
        verbose_name = 'Специалиста'
        verbose_name_plural = 'Специалисты'

    doctorFullName = models.CharField('Фамилия Имя Отчество', max_length=256)
    firstName = models.CharField('Имя', max_length=128)
    secondName = models.CharField('Фамилия', max_length=128)
    lastName = models.CharField('Отчество ', max_length=128)
    doctorPhoneNumber = models.PositiveIntegerField('Номер телефона')
    doctorEducation = models.TextField('Образование')
    doctorImage = models.ImageField(upload_to='doctorsImage/', null=True)
    doctorInfo = models.TextField('Информация о специалиста')
    doctorStatus = models.CharField('Статус специалиста', max_length=128)
    doctorWorkLocation = models.CharField('Адресс работы специалиста', max_length=512)
    doctorType = models.ForeignKey('DoctorType', on_delete=models.SET_NULL, null=True,
                                   verbose_name='Профессия специалиста')
    medical_staff_positions = models.ForeignKey('MedicalStaffPositions', on_delete=models.SET_NULL, null=True,
                                                verbose_name='Должность')
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   verbose_name='Пользователь')

    def __str__(self):
        return self.doctorFullName


class MedicalStaffPositions(models.Model):
    class Meta:
        verbose_name = 'Должность специалиста'
        verbose_name_plural = 'Должности специалистов'

    name = models.CharField('Должность специалиста', max_length=256)
    medical_staff_count = models.PositiveIntegerField('Количество объявлений', editable=False, default=0)
    image = models.ImageField(upload_to='medical_staff/', null=True)

    def __str__(self):
        return self.name


class DoctorType(models.Model):
    class Meta:
        verbose_name = 'Профессия специалиста'
        verbose_name_plural = 'Профессии специалистов'

    name = models.CharField('Название специалиста', max_length=256)
    image = models.ImageField(upload_to='doctor_type/', null=True)

    def __str__(self):
        return self.name
