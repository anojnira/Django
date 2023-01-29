from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'notes')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'notes': forms.Textarea(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'notes': 'Input your thoughts here'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django!')
        return title