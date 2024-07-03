from django import forms
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data.get('email')
        if data is None:
            raise ValidationError('Email is required')
        
        # you can also use serialiers to validate your data against the schema here
        return self.cleaned_data