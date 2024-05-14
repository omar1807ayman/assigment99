from django.db import models

class ClientType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

class Client(models.Model):
    name = models.CharField(max_length=200)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.product_name} ordered by {self.client.name}"
