from django import forms
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('real_estate','title','body','quote','image',)
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control input-md'}),
            'quote':forms.TextInput(attrs={'class': 'form-control input-md'}),
            'body' :forms.Textarea(attrs={'class': 'form-control', 'rows': '12', 'cols': '150'}),
            'image':forms.FileInput(attrs={'class': 'input-file','type':'file'}),
            'real_estate':forms.Select(attrs={'class': 'form-control'}),
        }


