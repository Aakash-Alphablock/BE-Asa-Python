from django import forms
from django.core.exceptions import ValidationError

class BotForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data.get('name')
        if data is None:
            raise ValidationError('Name is required')
        
        # you can also use serialiers to validate your data against the schema here
        return self.cleaned_data