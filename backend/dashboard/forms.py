from django import forms
from .models import Category,Folders, Links

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name', 'color']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folders
        fields = ['title', 'subheading', 'description', 'color']


class LinksForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['title', 'link']


