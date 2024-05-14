from django import forms
from .models import Client, ClientType, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'client_type']

class ClientTypeForm(forms.ModelForm):
    class Meta:
        model = ClientType
        fields = '__all__'

class ProductForm(forms.ModelForm):
    PRODUCT_CATEGORIES = [
        ('food', 'Food'),
        ('snacks', 'Snacks'),
        ('drinks', 'Drinks'),
        ('hardware', 'Hardware'),
    ]

    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'rating']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'category': forms.Select(choices=PRODUCT_CATEGORIES)
        }
        labels = {
            'product_name': 'Product Name',
            'category': 'Category',
            'description': 'Description',
            'rating': 'Rating'
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
