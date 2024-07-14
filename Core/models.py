from django.db import models

# Create your models here.

class ServiceCategory(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)

    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

class Service(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)

    Category = models.ForeignKey(ServiceCategory,on_delete=models.SET_NULL, null=True)
    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Title
