from django.db import models

# Create your models here.
class ServiceCall(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    
    Name = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Number = models.CharField(max_length=20)
    Email = models.EmailField(null=True)
    Description = models.TextField()