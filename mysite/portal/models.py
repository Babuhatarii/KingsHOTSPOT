from django.db import models
from django.utils.timezone import now
from datetime import timedelta

#A model for plans
class Plan(models.Model):
    name = models.CharField(max_length=50)  # e.g., "1 Hour Plan"
    duration_minutes = models.PositiveIntegerField()  # Duration in minutes
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Cost of the plan in KES

    def __str__(self):
        return self.name

#A model for payment
class Payment(models.Model):
    TRANSACTION_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    ]

    phone_number = models.CharField(max_length=15)  # User's phone number
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid
    transaction_id = models.CharField(max_length=100, unique=True)  # M-Pesa transaction ID
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS_CHOICES, default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)  # When payment was made

    def __str__(self):
        return self.transaction_id

#A model for sessions
class Session(models.Model):
    mac_address = models.CharField(max_length=17, unique=True)  # Device MAC address
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)  # Plan purchased
    start_time = models.DateTimeField()  # When the session started
    end_time = models.DateTimeField()  # When the session expires

    def __str__(self):
        return f"Session for {self.mac_address}"

