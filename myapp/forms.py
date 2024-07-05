# forms.py in myapp
from django import forms
from myapp.models import Product, User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = '__all__'
