from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserSubmittedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')])
    timestamp = models.DateTimeField(auto_now_add=True)
    ticket_number = models.IntegerField()
    resolved = models.BooleanField(default=False) 
    adminview = models.BooleanField(default= True)

    def __str__(self):
        return self.subject
    

class RespondedData(models.Model):
    user_data = models.ForeignKey(UserSubmittedData, on_delete=models.CASCADE)
    response = models.TextField()
    response_time = models.DateTimeField(auto_now_add=True)
    resolved= models.BooleanField(default=True)

    def __str__(self):
        return self.user_data.subject
