from django.db import models
from ckeditor.fields import RichTextField


class Room(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard Xona'),
        ('deluxe', 'Deluxe Xona'),
        ('suite', 'Suite Xona'),
        ('family', 'Oila uchun Xona'),
        ('presidential', 'Prezidentlik Xona'),
        ('business', 'Business Xona'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Nomi')
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, verbose_name='Xona turi')
    subtitle = models.CharField(max_length=200, verbose_name='Qisqa tavsif')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Narx (so\'m)')
    image = models.ImageField(upload_to='room_images/', verbose_name='Asosiy rasm')
    description = RichTextField(verbose_name='To\'liq tavsif')
    area = models.CharField(max_length=50, verbose_name='Maydoni')
    bed_type = models.CharField(max_length=100, verbose_name='Krevat turi')
    features = models.JSONField(default=list, verbose_name='Imkoniyatlar')
    is_active = models.BooleanField(default=True, verbose_name='Faol')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Xona'
        verbose_name_plural = 'Xonalar'
        ordering = ['price']
    
    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('rooms', 'Xonalar'),
        ('restaurant', 'Restoran'),
        ('spa', 'SPA & Fitness'),
        ('events', 'Tadbirlar'),
        ('other', 'Boshqa'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    image = models.ImageField(upload_to='gallery_images/', verbose_name='Rasm')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Kategoriya')
    is_active = models.BooleanField(default=True, verbose_name='Faol')
    order = models.PositiveIntegerField(default=0, verbose_name='Tartib')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Galereya rasmi'
        verbose_name_plural = 'Galereya rasmlari'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title


class StaffMember(models.Model):
    name = models.CharField(max_length=200, verbose_name='F.I.Sh.')
    position = models.CharField(max_length=200, verbose_name='Lavozim')
    image = models.ImageField(upload_to='staff_images/', verbose_name='Rasm')
    bio = models.TextField(verbose_name='Biografiya')
    telegram = models.URLField(blank=True, verbose_name='Telegram')
    instagram = models.URLField(blank=True, verbose_name='Instagram')
    linkedin = models.URLField(blank=True, verbose_name='LinkedIn')
    is_active = models.BooleanField(default=True, verbose_name='Faol')
    order = models.PositiveIntegerField(default=0, verbose_name='Tartib')
    
    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'
        ordering = ['order']
    
    def __str__(self):
        return self.name


class Service(models.Model):
    # FontAwesome iconlar ro'yxati
    ICON_CHOICES = [
        ('fas fa-wifi', 'Wi-Fi'),
        ('fas fa-utensils', 'Restoran / Ovqat'),
        ('fas fa-spa', 'SPA'),
        ('fas fa-dumbbell', 'Fitness'),
        ('fas fa-swimming-pool', 'Hovuz'),
        ('fas fa-car', 'Avtoturargoh'),
        ('fas fa-concierge-bell', 'Xonam xizmati'),
        ('fas fa-shuttle-van', 'Transfer'),
        ('fas fa-snowflake', 'Konditsioner'),
        ('fas fa-tv', 'Televizor'),
        ('fas fa-phone', 'Telefon'),
        ('fas fa-glass-martini', 'Bar'),
        ('fas fa-coffee', 'Kofe / Choy'),
        ('fas fa-umbrella-beach', 'Plaj'),
        ('fas fa-parking', 'Parkovka'),
        ('fas fa-wheelchair', 'Nogironlar uchun'),
        ('fas fa-paw', 'Hayvonlar uchun'),
        ('fas fa-baby', 'Bolalar uchun'),
        ('fas fa-business-time', 'Business markaz'),
        ('fas fa-credit-card', 'Karta to\'lovi'),
        ('fas fa-lock', 'Seif'),
        ('fas fa-tshirt', 'Kir yuvish'),
        ('fas fa-dryer', 'Kir yuvish xizmati'),
        ('fas fa-iron', 'Dazmol'),
        ('fas fa-hair-dryer', 'Soch quritgich'),
        ('fas fa-bath', 'Vanna / Dush'),
        ('fas fa-toilet', 'Hojatxona'),
        ('fas fa-bed', 'Qo\'shimcha krevat'),
        ('fas fa-couch', 'Divan'),
        ('fas fa-fan', 'Ventilyator'),
        ('fas fa-thermometer-half', 'Isitish / Sovutish'),
        ('fas fa-wind', 'Konditsioner'),
        ('fas fa-music', 'Muzika'),
        ('fas fa-gamepad', 'O\'yinlar'),
        ('fas fa-book', 'Kutubxona'),
        ('fas fa-newspaper', 'Gazeta / Jurnal'),
        ('fas fa-laptop', 'Noutbuk'),
        ('fas fa-print', 'Printer'),
        ('fas fa-fax', 'Faks'),
        ('fas fa-wifi', 'Internet'),
        ('fas fa-ethernet', 'Ethernet'),
        ('fas fa-satellite-dish', 'Sun\'iy yo\'ldosh TV'),
        ('fas fa-video', 'Video'),
        ('fas fa-film', 'Kino'),
        ('fas fa-camera', 'Kamera'),
        ('fas fa-binoculars', 'Kuzatuv'),
        ('fas fa-guard', 'Xavfsizlik'),
        ('fas fa-user-shield', 'Shaxsiy xavfsizlik'),
        ('fas fa-fire-extinguisher', 'Yong\'in xavfsizligi'),
        ('fas fa-first-aid', 'Tibbiy yordam'),
        ('fas fa-ambulance', 'Tez tibbiy yordam'),
        ('fas fa-pills', 'Dorixona'),
        ('fas fa-hospital', 'Shifoxona'),
        ('fas fa-clinic-medical', 'Klinika'),
        ('fas fa-stethoscope', 'Shifokor'),
        ('fas fa-heartbeat', 'Salomatlik'),
        ('fas fa-spa', 'Massaj'),
        ('fas fa-hot-tub', 'Jakuzi'),
        ('fas fa-sauna', 'Sauna'),
        ('fas fa-steam', 'Bug\''),
        ('fas fa-sink', 'Rakovina'),
        ('fas fa-shower', 'Dush'),
        ('fas fa-bath', 'Vanna'),
        ('fas fa-soap', 'Soat'),
        ('fas fa-hand-sparkles', 'Toza qo\'llar'),
        ('fas fa-pump-soap', 'Suyuq soat'),
        ('fas fa-toilet-paper', 'Hojatxona qog\'ozi'),
        ('fas fa-trash', 'Axlat'),
        ('fas fa-recycle', 'Qayta ishlash'),
        ('fas fa-leaf', 'Ekologik toza'),
        ('fas fa-solar-panel', 'Quyosh energiyasi'),
        ('fas fa-charging-station', 'Zaryadlash stansiyasi'),
        ('fas fa-battery-full', 'Batareya'),
        ('fas fa-plug', 'Rozetka'),
        ('fas fa-lightbulb', 'Chiroq'),
        ('fas fa-sun', 'Quyosh'),
        ('fas fa-moon', 'Oy'),
        ('fas fa-cloud', 'Bulut'),
        ('fas fa-rain', 'Yomg\'ir'),
        ('fas fa-snowflake', 'Qor'),
        ('fas fa-wind', 'Shamol'),
        ('fas fa-temperature-high', 'Issiq'),
        ('fas fa-temperature-low', 'Sovuq'),
        ('fas fa-thermometer', 'Termometr'),
        ('fas fa-fire', 'Olov'),
        ('fas fa-fire-alt', 'Olov 2'),
        ('fas fa-burn', 'Yonish'),
        ('fas fa-water', 'Suv'),
        ('fas fa-tint', 'Tomchi'),
        ('fas fa-tint-slash', 'Yopiq tomchi'),
        ('fas fa-droplet', 'Tomchi 2'),
        ('fas fa-oil-can', 'Yog\''),
        ('fas fa-gas-pump', 'Yoqilg\'i'),
        ('fas fa-gas-pump-slash', 'Yoqilg\'i yo\'q'),
        ('fas fa-charging-station', 'Zaryadlash'),
        ('fas fa-bolt', 'Elektr'),
        ('fas fa-plug', 'Rozetka'),
        ('fas fa-power-off', 'O\'chirish'),
        ('fas fa-toggle-on', 'Yoqish'),
        ('fas fa-toggle-off', 'O\'chirish'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Nomi')
    icon = models.CharField(
        max_length=50, 
        choices=ICON_CHOICES, 
        default='fas fa-wifi',
        verbose_name='Icon'
    )
    description = models.TextField(verbose_name='Tavsif')
    is_active = models.BooleanField(default=True, verbose_name='Faol')
    
    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = 'Xizmatlar'
    
    def __str__(self):
        return self.title
    
    # Admin panelda icon ko'rsatish uchun
    def icon_preview(self):
        from django.utils.html import format_html
        return format_html('<i class="{} text-2xl text-yellow-600"></i>', self.icon)
    icon_preview.short_description = 'Icon ko\'rinishi'


class ContactInfo(models.Model):
    address = models.TextField(verbose_name='Manzil')
    phone = models.CharField(max_length=50, verbose_name='Telefon')
    email = models.EmailField(verbose_name='Email')
    working_hours = models.TextField(verbose_name='Ish vaqti')
    
    class Meta:
        verbose_name = 'Aloqa ma\'lumotlari'
        verbose_name_plural = 'Aloqa ma\'lumotlari'
    
    def __str__(self):
        return 'Aloqa ma\'lumotlari'
    
    
