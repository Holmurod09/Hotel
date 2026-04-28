from django import forms


class IconSelectWidget(forms.Select):
    template_name = 'core/widgets/icon_select.html'
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['icons'] = self.choices
        return context