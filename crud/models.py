from django.db import models

# Create your models here.
class Menu(models.Model):
    menu = models.CharField(max_length=100)
    calorie = models.FloatField()
    date = models.DateField()
    
    def __str__(self):
        return self.menu