from django.contrib import admin
from .models import Room, GalleryImage, StaffMember, Service, ContactInfo


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['title', 'room_type', 'price', 'is_active']
    list_filter = ['room_type', 'is_active']
    search_fields = ['title', 'description']
    list_editable = ['is_active']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'order']
    list_filter = ['category', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['name', 'position']



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_preview', 'icon', 'is_active']
    list_editable = ['is_active']
    search_fields = ['title']
    
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'is_active')
        }),
        ('Icon tanlash', {
            'fields': ('icon',),
            'description': 'Xizmat uchun mos iconni tanlang. <a href="https://fontawesome.com/icons" target="_blank">Barcha iconlar</a>',
        }),
    )

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css',
            )
        }


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()
    

