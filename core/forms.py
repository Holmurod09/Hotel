from django import forms
from .models import Service
from .widgets import IconSelectWidget


class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'icon': IconSelectWidget(choices=Service.ICON_CHOICES),
        }