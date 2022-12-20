from django.db import models

# Create your models here.
#! models.py'deki her class database'de bir tablo'dur
#* classlardaki her instance tablonun bir satırıdır.

class Classname(models.Model):
  pass # hiçbirşey yazılmayacaksa pass yazılır. Format bu

class Student(models.Model):
  first_name = models.CharField(max_length=50) #! field
  last_name = models.CharField(max_length=50)
  number = models.IntegerField(default=1111) # default değer atandı, yazılmazsa 1111 alır
  about = models.TextField(blank=True, null=True) # boş bırakılabilir, null olabilir.
  register = models.DateTimeField(auto_now_add=True) # auto_now_add : oluşturulan tarih/saati 1 kere alır
  last_updated_date = models.DateTimeField(auto_now=True) # auto_now : güncellenen tarih/saati her güncellemede alır
  is_active = models.BooleanField()
  
  def __str__(self):
    return f"{self.number} + {self.first_name}"
  
  class Meta:
    ordering = ["number"]
    verbose_name_plural = "Student_list"
    
  def student_year_status(self):
    "Returns the student's year status"
    import datetime
    if self.register < datetime.date(2019, 1, 1):
      return "Senior"
    if self.register > datetime.date(2020, 1, 1):
      return "Junior"
    else:
      return "Freshman"