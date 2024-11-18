from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Bus(models.Model):
    busnumber = models.CharField(max_length=100,null=True)
    seating_capacity = models.IntegerField(null=True)
    route = models.CharField(max_length=100,null=True)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    

    

    def __str__(self):
        return self.busnumber