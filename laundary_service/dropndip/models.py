from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    men_count = models.PositiveIntegerField()
    women_count = models.PositiveIntegerField()
    pickup_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    total_amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ₹{self.total_amount}"
