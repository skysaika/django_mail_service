from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Customer(models.Model):
    """
    Client Model - модель клиентов
    email: почта
    first_name: фамилия
    last_name: имя
    surname: отчество
    comment: Комментарий
    """
    CUSTOMER_STATUS = [
        (True, 'Активен'),
        (False, 'Заблокирован')
    ]

    email = models.EmailField(verbose_name='Почта', unique=True)
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=40, verbose_name='Отчество', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    # Атрибут для блокировки пользователя менеджером
    is_active = models.BooleanField(default=True, choices=CUSTOMER_STATUS, verbose_name='Статус пользователя')

    def __str__(self):
        return f'{self.email} {self.first_name} {self.surname}'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервиса'
        ordering = ('pk',)


class MailingSettings(models.Model):
    """
    Модель настроек рассылки
    customers: клиенты
    send_time: время рассылки
    frequency: периодичность
    sending_status: статус отправки
    message_title: тема письма
    message_content: содержание
    mailing_owner: создатель рассылки
    """
    STATUS_CHOICES = [
        (None, 'Не указано'),
        ('created', 'Создана'),
        ('active', 'Запущена'),
        ('closed', 'Завершена')
    ]

    FREQUENCY_CHOICES = [
        (None, 'Не указано'),
        ('OPD', 'Раз в день'),
        ('OPW', 'Раз в неделю'),
        ('OPM', 'Раз в месяц')
    ]

    customers = models.ManyToManyField('Customer', verbose_name='Клиенты')

    # Атрибуты для настройки рассылки
    send_time = models.DateTimeField(default=timezone.now, verbose_name='Время рассылки')

    frequency = models.CharField(
        max_length=3, choices=FREQUENCY_CHOICES, default=None, verbose_name='Периодичность'
    )

    sending_status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, default=None, verbose_name='Статус отправки'
    )

    # Атрибуты для создания письма в рассылке
    message_title = models.CharField(max_length=250, verbose_name='Тема письма')
    message_content = models.TextField(verbose_name='Содержание')

    # Атрибут для связи создатель-рассылка
    mailing_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Создатель рассылки')

    def __str__(self):
        return f'Периодичность: {self.frequency}. Статус отправки: {self.sending_status}'

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылок'
        ordering = ('sending_status',)
