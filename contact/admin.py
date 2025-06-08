from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('Timestamp', {
            'fields': ('created_at',)
        }),
    )

    def has_add_permission(self, request):
        return False
