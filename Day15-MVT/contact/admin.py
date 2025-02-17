from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Fields to show in admin
    readonly_fields = ('name', 'email', 'message')  # Make fields read-only

    def has_add_permission(self, request):
        return False  # Disable add button

    def has_change_permission(self, request, obj=None):
        return False  # Disable edit option

    def has_delete_permission(self, request, obj=None):
        return False  # Disable delete option

admin.site.register(Contact, ContactAdmin)