from typing import Any
from django.contrib import admin

from common import admin as common_admin

# Register your models here.

from user import models
from user import forms

@admin.register(models.UserProfile)
class AdminBot(common_admin.ReadOnlyUpdatedCreatedAdmin):
    form = forms.UserForm
    list_display = ['id', 'email', 'first_name', 'last_name', 'created_at',]
    search_fields = ['email', 'id']

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        # you can add custom logic here like invalidating cache or creating a log entry etc.
        return super().save_model(request, obj, form, change)
