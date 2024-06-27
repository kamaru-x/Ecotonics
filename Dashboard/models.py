from django.db import models

# Create your models here.

class Site(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=50,default='PENDING')

    Name = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Contact = models.CharField(max_length=20)
    Mail = models.EmailField(null=True)

    def __str__(self):
        return self.Name
    
class Transaction_Category(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)

    Title = models.CharField(max_length=50)
    Type = models.CharField(max_length=20)

    def __str__(self):
        return self.Title
    
class Transaction(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)

    Title = models.CharField(max_length=50)
    Description = models.TextField(null=True)
    Category = models.ForeignKey(Transaction_Category,on_delete=models.SET_NULL, null=True)
    Amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.Title