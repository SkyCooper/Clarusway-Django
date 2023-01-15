from django.db import models

# Create your models here.
class Creator(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Languages(models.Model):
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Frameworks(models.Model):
    languages = models.ForeignKey(Languages, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
      
class Programmer(models.Model):
    framework = models.ManyToManyField(Frameworks, db_table="dd")
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)