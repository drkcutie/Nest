from django import forms
from .models import Category, Tags

class CategoryForm(forms.ModelForm):
    

    class Meta:
        model = Category
        fields = ['name', 'color']

