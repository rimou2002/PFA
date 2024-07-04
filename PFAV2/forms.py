# forms.py in myapp
from django import forms
from myapp.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
