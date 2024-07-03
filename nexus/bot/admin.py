from typing import Any
from django.contrib import admin

from common import admin as common_admin

# Register your models here.
from bot import models
from bot import forms

@admin.register(models.Bot)
class AdminBot(common_admin.ReadOnlyUpdatedCreatedAdmin):
    form = forms.BotForm
    list_display = ['id', 'name', 'description', 'user_id', 'is_demo_bot', 'is_deleted', 'created_at', 'updated_at'] # token is not to be shown so removed from list_display
    list_filter = ['name', 'user_id', 'is_demo_bot', 'is_deleted']
    search_fields = ['name', 'user_id', 'is_demo_bot', 'is_deleted']

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        # you can add custom logic here like invalidating cache or creating a log entry etc.
        return super().save_model(request, obj, form, change)



