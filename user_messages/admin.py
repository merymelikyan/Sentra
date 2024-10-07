from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','content', 'timestamp')
    search_fields = ('name', 'email', 'subject', 'content')
    list_filter = ('timestamp',)
