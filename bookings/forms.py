from django import forms
from django.core.validators import RegexValidator
from core.models import Room
from .models import Booking


class BookingForm(forms.ModelForm):
    country_code = forms.ChoiceField(
        choices=Booking.COUNTRY_CODES,
        initial='+998',
        widget=forms.Select(attrs={
            'class': 'country-select px-3 py-3 rounded-l-lg bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all cursor-pointer',
            'style': 'min-width: 140px;'
        }),
        label='Davlat'
    )
    
    phone = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[\d\s\-]{7,}$',
                message='Telefon raqam faqat raqamlardan iborat bo\'lishi kerak',
                code='invalid_phone'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'phone-input w-full px-4 py-3 rounded-r-lg bg-gray-50 dark:bg-dark border border-l-0 border-gray-200 dark:border-gray-700 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all',
            'placeholder': '90 123 45 67'
        }),
        label='Telefon raqam'
    )
    
    contact_method = forms.ChoiceField(
        choices=Booking.CONTACT_METHODS,
        initial='whatsapp',
        widget=forms.RadioSelect(),
        label='Aloqa usuli'
    )
    
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'country_code', 'phone', 'contact_method', 'room', 'check_in', 'check_out', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-dark border border-gray-200 dark:border-gray-700 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all',
                'placeholder': 'Ismingiz'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-dark border border-gray-200 dark:border-gray-700 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all',
                'placeholder': 'Familiyangiz'
            }),
            'room': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-dark border border-gray-200 dark:border-gray-700 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all'
            }),
            'check_in': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-dark border border-gray-200 dark:border-gray-700 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all'
            }),
            'check_out': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-dark border border-gray-200 dark:border-gray-700 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-dark border border-gray-200 dark:border-gray-700 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all resize-none',
                'rows': 4,
                'placeholder': 'Maxsus so\'rovlaringiz...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.filter(is_active=True)
        self.fields['room'].empty_label = "Xona tanlang"
    
    def clean_phone(self):
        """Telefon raqamni tozalash"""
        phone = self.cleaned_data.get('phone', '')
        # Faqat raqamlarni olish
        phone = ''.join(filter(str.isdigit, phone))
        return phone