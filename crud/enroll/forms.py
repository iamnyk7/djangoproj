from django import forms
from .models import crud
# from django.core import validators

class crudreg(forms.ModelForm):
    
    class Meta:
        model = crud
        fields = ["title","key","desc"]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'key':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.TextInput(attrs={'class':'form-control'}),
        }

