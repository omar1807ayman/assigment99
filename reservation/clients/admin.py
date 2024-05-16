from django.contrib import admin
from .models import Client, ClientType, Product, Order

admin.site.register(Client)
admin.site.register(ClientType)
admin.site.register(Product)
admin.site.register(Order)
