from django.db import models

# Create your models here.
#! models.py'deki her class database'de bir tablo'dur
#* classlardaki her instance tablonun bir sütünudur..

class Classname(models.Model):
  pass # hiçbirşey yazılmayacaksa pass yazılır. Format bu

class Student(models.Model): #!Student isimli bir tablo oluştu db içinde
  first_name = models.CharField(max_length=50) #! Tablonun sütunları, field'lar
  last_name = models.CharField(max_length=50) #! içindekiler field option type
  number = models.IntegerField(default=1111) # default değer atandı, yazılmazsa 1111 alır
  
  about = models.TextField(blank=True, null=True) # boş bırakılabilir, null olabilir.
  #?------------- blank=True , null=True ----------------
  # blank=True, serializer ile ilgilidir, yani boş bırakılabilir,
  # null=True, DB ile ilgilidir, yani boş bırakılabilir ve DB null kayıt edilir,
  #! eğer sadece  blank=True varsa veri boş gelebilir, ama DB kayıt edilmeden önce
  #! bir işlem/hesaplama vs. yapılıp DB boş/null gitmesini önlemek gerekir.
  
  register = models.DateTimeField(auto_now_add=True) # auto_now_add : oluşturulan tarih/saati 1 kere alır
  last_updated_date = models.DateTimeField(auto_now=True) # auto_now : güncellenen tarih/saati her güncellemede alır
  is_active = models.BooleanField()
                                                     # DateTimeField tarih/saat DateField sadece tarih
  #? str medotu ile tablonun admin panelde nasıl görüneceğini ayarlıyoruz.
  #? str medotunda yapılan değişiklik db değiştirmiyor, 
  #? bunun için migrate komutlarını tekrar çalıştırmaya gerek kalmıyor. 
  def __str__(self):
    return f"{self.number} {self.first_name}"
  
  #? indentation dikkat class içinde yazıyoruz Meta'yı.
  #? ana classın bazı optionlarını buradan ayarlayabiliyoruz.
  #? db'de değişiklik yapan bir option ise migrate komutları yeniden çalışması gerekli
  #? alttakiler db'de değişiklik yapmıyor. (sadece görünüşü değiştiriyor.)
  
  class Meta:
    ordering = ["number"] #? ordering : numaraya göre sırala
    verbose_name_plural = "Student_list" #? verbose_name_plural : Student olan isim Student_list oldu admi panelde.
  
  
  #? method ekleme,
  #? miras olarak alabilir, veya override edebiliriz.
  #? en çok override edilen save() ve delete() metodlarıdır.
  #? ilave bir method ekliyoruz,
  def student_year_status(self):
    "Returns the student's year status"
    import datetime
    if self.register < datetime.date(2019, 1, 1):
      return "Senior"
    if self.register > datetime.date(2020, 1, 1):
      return "Junior"
    else:
      return "Freshman"