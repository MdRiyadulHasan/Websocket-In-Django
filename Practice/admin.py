from django.contrib import admin
from chat.models import Group, ChatInfo

# Register your models here.
@admin.register(ChatInfo)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'timestamp', 'group']

@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

