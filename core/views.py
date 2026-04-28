from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.http import JsonResponse
from .models import Room, GalleryImage, StaffMember, Service, ContactInfo


class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.filter(is_active=True)[:3]
        context['services'] = Service.objects.filter(is_active=True)[:6]
        context['gallery'] = GalleryImage.objects.filter(is_active=True)[:6]
        context['staff'] = StaffMember.objects.filter(is_active=True)[:4]
        return context


class RoomListView(ListView):
    model = Room
    template_name = 'core/rooms.html'
    context_object_name = 'rooms'
    
    def get_queryset(self):
        return Room.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # JSON formatda xonalar ma'lumotini JS uchun
        rooms_data = []
        for room in context['rooms']:
            rooms_data.append({
                'id': room.id,
                'title': room.title,
                'subtitle': room.subtitle,
                'price': str(room.price),
                'image': room.image.url if room.image else '',
                'description': str(room.description),
                'features': room.features,
                'area': room.area,
                'bed_type': room.bed_type,
            })
        context['rooms_json'] = rooms_data
        return context


# API endpoint for room details (modal uchun)
def room_detail_api(request, pk):
    room = get_object_or_404(Room, pk=pk, is_active=True)
    data = {
        'id': room.id,
        'title': room.title,
        'subtitle': room.subtitle,
        'price': str(room.price),
        'image': room.image.url if room.image else '',
        'description': str(room.description),
        'features': room.features,
        'area': room.area,
        'bed_type': room.bed_type,
    }
    return JsonResponse(data)


class GalleryView(ListView):
    model = GalleryImage
    template_name = 'core/gallery.html'
    context_object_name = 'images'
    
    def get_queryset(self):
        return GalleryImage.objects.filter(is_active=True).order_by('order', '-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = dict(GalleryImage.CATEGORY_CHOICES)
        # JSON formatda galereya ma'lumotlari
        gallery_data = []
        for img in context['images']:
            gallery_data.append({
                'src': img.image.url if img.image else '',
                'title': img.title,
                'category': img.category,
            })
        context['gallery_json'] = gallery_data
        return context


class StaffView(ListView):
    model = StaffMember
    template_name = 'core/staff.html'
    context_object_name = 'staff_members'
    
    def get_queryset(self):
        return StaffMember.objects.filter(is_active=True).order_by('order')


class ServicesView(ListView):
    model = Service
    template_name = 'core/services.html'
    context_object_name = 'services'
    
    def get_queryset(self):
        return Service.objects.filter(is_active=True)


class ContactView(TemplateView):
    template_name = 'core/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        context['rooms'] = Room.objects.filter(is_active=True)
        return context