from django.contrib import admin

from mailing.models import Customer, MailingSettings, MessagesLogs


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer admin"""
    list_display = ('pk', 'first_name', 'surname', 'patronymic', 'email',)
    list_display_links = ('first_name', 'surname', 'patronymic',)
    search_fields = ('email',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    """Mailing settings admin"""
    list_display = ('pk', 'send_time', 'frequency', 'sending_status',)
    list_display_links = ('pk',)
    filter_horizontal = ('customers',)
    list_editable = ('frequency', 'sending_status',)
    list_filter = ('frequency', 'sending_status',)


@admin.register(MessagesLogs)
class MessagesLogsAdmin(admin.ModelAdmin):
    """Messages logs admin"""
    list_display = ('pk', 'last_attempt_time', 'attempt_status', 'server_response',)
    list_display_links = ('attempt_status',)
    list_filter = ('last_attempt_time', 'attempt_status', 'server_response',)
