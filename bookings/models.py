from django.db import models
from core.models import Room


class Booking(models.Model):
    CONTACT_METHODS = [
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
    ]
    
    # Davlat kodlari
    COUNTRY_CODES = [
        ('+998', '🇺🇿 O\'zbekiston (+998)'),
        ('+7', '🇷🇺 Rossiya (+7)'),
        ('+1', '🇺🇸 AQSh (+1)'),
        ('+44', '🇬🇧 Buyuk Britaniya (+44)'),
        ('+49', '🇩🇪 Germaniya (+49)'),
        ('+90', '🇹🇷 Turkiya (+90)'),
        ('+86', '🇨🇳 Xitoy (+86)'),
        ('+91', '🇮🇳 Hindiston (+91)'),
        ('+81', '🇯🇵 Yaponiya (+81)'),
        ('+82', '🇰🇷 Koreya (+82)'),
        ('+971', '🇦🇪 BAA (+971)'),
        ('+992', '🇹🇯 Tojikiston (+992)'),
        ('+993', '🇹🇲 Turkmaniston (+993)'),
        ('+996', '🇰🇬 Qirg\'iziston (+996)'),
        ('+994', '🇦🇿 Ozarbayjon (+994)'),
        ('+375', '🇧🇾 Belarus (+375)'),
        ('+380', '🇺🇦 Ukraina (+380)'),
        ('+48', '🇵🇱 Polsha (+48)'),
        ('+39', '🇮🇹 Italiya (+39)'),
        ('+33', '🇫🇷 Fransiya (+33)'),
        ('+34', '🇪🇸 Ispaniya (+34)'),
    ]
    
    first_name = models.CharField(max_length=100, verbose_name='Ism')
    last_name = models.CharField(max_length=100, verbose_name='Familiya')
    country_code = models.CharField(
        max_length=5, 
        choices=COUNTRY_CODES,
        default='+998',
        verbose_name='Davlat kodi'
    )
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHODS, verbose_name='Aloqa usuli')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Xona')
    check_in = models.DateField(null=True, blank=True, verbose_name='Kelish sanasi')
    check_out = models.DateField(null=True, blank=True, verbose_name='Ketish sanasi')
    message = models.TextField(blank=True, verbose_name='Xabar')
    is_processed = models.BooleanField(default=False, verbose_name='Ko\'rib chiqildi')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Bron'
        verbose_name_plural = 'Bronlar'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.room.title}"
    
    def get_full_phone(self):
        """To'liq telefon raqam"""
        return f"{self.country_code} {self.phone}"