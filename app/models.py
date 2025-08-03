from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True,blank=True, default="null")
    address = models.CharField(max_length=255, null=True, blank=True, default="null")
    role = models.CharField(max_length=50, default='user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Farm(models.Model):
    farm_id = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='farms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.farm_id
    
class Irrigation(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='irrigations')
    volume_used = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.irrigation_id
    
class Fertilizer(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='fertilizers')
    type = models.CharField(max_length=100)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.quantity} kg"
    
class PestControl(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='pest_controls')
    type = models.CharField(max_length=100)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.quantity} kg"
    
class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:20]}..."
