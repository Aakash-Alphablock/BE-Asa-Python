from django.contrib import admin
class ReadOnlyUpdatedCreatedAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']