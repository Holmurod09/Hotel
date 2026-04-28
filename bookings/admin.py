from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country_code', 'phone', 'full_phone', 'room', 'contact_method', 'is_processed', 'created_at']
    list_filter = ['is_processed', 'contact_method', 'country_code', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone']
    list_editable = ['is_processed']
    date_hierarchy = 'created_at'
    
    def full_phone(self, obj):
        """To'liq telefon ko'rinishi"""
        return obj.get_full_phone()
    full_phone.short_description = 'To\'liq telefon'