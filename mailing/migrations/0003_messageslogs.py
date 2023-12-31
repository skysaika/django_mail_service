# Generated by Django 4.2.3 on 2023-07-31 16:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_mailingsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagesLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время последней попытки')),
                ('attempt_status', models.CharField(choices=[(None, 'Не указано'), ('received', 'Получено'), ('failed', 'Провалено')], default=None, max_length=8, verbose_name='Статус попытки')),
                ('server_response', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ответ сервера')),
                ('mailing_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='Настройки рассылки')),
            ],
            options={
                'verbose_name': 'Логи рассылки',
                'verbose_name_plural': 'Логи рассылок',
                'ordering': ('attempt_status',),
            },
        ),
    ]
