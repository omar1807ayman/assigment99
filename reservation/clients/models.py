from django.db import models

class ClientType(models.Model):
    type_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.type_name

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)
    joined_date = models.DateField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for {self.client.name}"
