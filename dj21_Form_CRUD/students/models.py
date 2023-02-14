from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.SmallIntegerField()
    image = models.ImageField(upload_to="students", blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
