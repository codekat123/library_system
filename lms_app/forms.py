from django import forms
from .models import *

class CategoryForms(forms.ModelForm):
    class Meta:
        model = category
        fields = ['type']
        widgets ={
            'type':forms.TextInput(attrs={'class':'form-control'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = [ 'active'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'autor_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_of_rent': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),        }
