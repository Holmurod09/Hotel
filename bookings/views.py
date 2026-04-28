from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm
from core.models import Room, ContactInfo


class BookingCreateView(FormView):
    """
    Contact sahifasida forma ko'rsatish va qayta yuborish
    """
    template_name = 'core/contact.html'
    form_class = BookingForm
    success_url = reverse_lazy('contact')  # Qaytib contact ga o'tadi
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        context['rooms'] = Room.objects.filter(is_active=True)
        # Form xatolari bilan birga uzatiladi
        return context
    
    def form_valid(self, form):
        """Form to'g'ri to'ldirilgan bo'lsa"""
        try:
            # Saqlash
            booking = form.save()
            
            # Email yuborish
            self.send_notification_email(booking)
            
            messages.success(self.request, 'Xabaringiz muvaffaqiyatli yuborildi! Tez orada bog\'lanamiz.')
            return redirect(self.get_success_url())
            
        except Exception as e:
            messages.error(self.request, f'Saqlashda xatolik: {str(e)}')
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        """Form xato bo'lsa — qaytib contact sahifasiga"""
        messages.error(self.request, 'Formani to\'ldirishda xatolik. Iltimos, barcha maydonlarni tekshiring.')
        
        # Kontekst bilan qayta render qilish (contact sahifasida)
        return self.render_to_response(self.get_context_data(form=form))
    
    def send_notification_email(self, booking):
        """Email xabar yuborish"""
        subject = f'Yangi bron: {booking.first_name} {booking.last_name}'
        message = f"""
MEHMONXONA BRON

Mijoz ma'lumotlari:
------------------
Ism: {booking.first_name}
Familiya: {booking.last_name}
Telefon: +998 {booking.phone}
Aloqa usuli: {booking.get_contact_method_display()}

Bron ma'lumotlari:
-----------------
Xona: {booking.room.title}
Kelish sanasi: {booking.check_in or 'Kiritilmagan'}
Ketish sanasi: {booking.check_out or 'Kiritilmagan'}

Xabar:
{booking.message or 'Yo\'q'}

Sana: {booking.created_at}
"""
        
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,  # Xatolikni e'tiborsiz qoldirish
            )
        except Exception as e:
            print(f"Email yuborishda xatolik: {e}")