from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='static/profile_pictures')

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name='customer')
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer} ordered {self.description}'
