from django.db import models

# Create your models here.
class Student(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=40)
  number = models.PositiveSmallIntegerField(blank=True, null=True)
  # blank = True değilse zorunlu alan olur, boş bırakılamaz
  # null = stringler default null olabilir numberler olmaz, fieldType null=True yapmak gerekli,
  about = models.TextField(blank=True)
  email = models.EmailField(blank=True)
  is_active = models.BooleanField(default=True) #! boolen field default tanımlamak mantıklı
  avatar = models.ImageField(blank=True, null=True, upload_to='student')
  # avatar = models.FileField(blank=True, null=True) #!FileField da kullanılabilir
  files = models.FileField(blank=True, null=True, upload_to='student_files')
  register_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f" {self.number} -{self.first_name} {self.last_name}"
  
  #? indentation dikkat class içinde yazıyoruz Meta'yı.
  #? ana classın bazı optionlarını buradan ayarlayabiliyoruz.
  #? db'de değişiklik yapan bir option ise migrate komutları yeniden çalışması gerekli
  #? alttakiler db'de değişiklik yapmıyor. (sadece görünüşü değiştiriyor.)
  
  class Meta:
    ordering = ("-number",) #? ordering : numaraya göre sırala - ise ters sırala
    verbose_name = "Öğrenci" #? verbose_name_plural : Student olan isim Öğrenci oldu admi panelde.
    verbose_name_plural = "Öğrenciler"
    # db_table = '' tablo ismini değiştirir, migrate gerekli

class Teacher(models.Model):
  pass

#! look-up's;
# repodan al...