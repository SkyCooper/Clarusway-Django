from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#! models.py'deki her class database'de bir tablo'dur
#* classlardaki her instance/field tablonun bir sütünudur..

class Classname(models.Model):
    pass # hiçbirşey yazılmayacaksa pass yazılır. Format bu

class Path(models.Model):
    path_name = models.CharField(max_length=50)
    # aşağıda class'da, yani child tabloda --> related_name='students' yazıyor olması  ;
    # students = ... (sanki böyle bir field varmış demektir.)

    def __str__(self):
        return f"{self.path_name}"

class Student(models.Model): #!Student isimli bir tablo oluştu db içinde
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50) #! Tablonun sütunları, field'lar
    last_name = models.CharField(max_length=50) #! içindekiler field option type
    number = models.IntegerField(default=1111) # default değer atandı, yazılmazsa 1111 alır
    
    about = models.TextField(blank=True, null=True) # boş bırakılabilir, null olabilir.
    #?------------- blank=True , null=True ----------------
    # blank=True, serializer ile ilgilidir, yani boş bırakılabilir,
    # null=True, DB ile ilgilidir, yani boş bırakılabilir ve DB null kayıt edilir,
    #! eğer sadece  blank=True varsa veri boş gelebilir, ama DB kayıt edilmeden önce
    #! bir işlem/hesaplama vs. yapılıp DB boş/null gitmesini önlemek gerekir.
    
    files = models.FileField(blank=True, null=True, upload_to='student_files')
    
    avatar = models.ImageField(blank=True, null=True, upload_to='student_pictures')
    # upload_to='student_pictures' => eklenecek resimler, media altında student_pictures diye bir klasöre kayıt edilsin demek
    
    # avatar = models.FileField(blank=True, null=True) #!FileField da kullanılabilir
    
    register_date = models.DateTimeField(auto_now_add=True) 
    # auto_now_add : oluşturulan tarih/saati 1 kere alır
    
    update_date = models.DateTimeField(auto_now=True)
    # auto_now : güncellenen tarih/saati her güncellemede alır
    # DateTimeField tarih/saat DateField sadece tarih
    
    is_active = models.BooleanField(default=True) 
    #boolen field default tanımlamak mantıklı True/False değer alır.
    
    

    #? str medotu ile tablonun admin panelde nasıl görüneceğini ayarlıyoruz.
    #? str medotunda yapılan değişiklik db değiştirmiyor, 
    #? bunun için migrate komutlarını tekrar çalıştırmaya gerek kalmıyor. 
    def __str__(self):
        return f"{self.number} {self.first_name}"
        # return {self.number}
        # return "{} {}".format(self.first_name, self.number)

    #? indentation dikkat class içinde yazıyoruz Meta'yı.
    #? ana classın bazı optionlarını buradan ayarlayabiliyoruz.
    #? db'de değişiklik yapan bir option ise migrate komutları yeniden çalışması gerekli
    #? alttakiler db'de değişiklik yapmıyor. (sadece görünüşü değiştiriyor.)

    class Meta:
        ordering = ["number"] #? ordering : numaraya göre sırala
        # ordering = ("-number",) # ordering : numaraya göre sırala - ise ters sırala
        verbose_name = "Öğrenci" #? verbose_name : Student olan isim Öğrenci oldu admin panelde.
        verbose_name_plural = "Öğrenciler" #? verbose_name_plural : Student olan isim Öğrenciler oldu admin panelde.
        # verbose_name_plural = "Student_list" # verbose_name_plural : Student olan isim Student_list oldu admi panelde.
        # db_table = '' tablo ismini değiştirir, migrate gerekli


    #? method ekleme,
    #? miras olarak alabilir, veya override edebiliriz.
    #? en çok override edilen save() ve delete() metodlarıdır.
    #? ilave bir method ekliyoruz,
    def student_year_status(self):
        """Returns the student's year status"""
        import datetime
        if self.register < datetime.date(2019, 1, 1):
            return "Senior"
        if self.register > datetime.date(2020, 1, 1):
            return "Junior"
        else:
            return "Freshman"



#! -------------------------------------------------------------------
#! -------------------  Models Relations Dj03 ------------------------
#! -------------------------------------------------------------------

class Profile(models.Model):
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile', blank=True, null=True) 
    # upload_to='profile' => eklenecek resimler, media altında profile diye bir klasör oluşsun 
    # ve oraya kayıt edilsin demek
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # hangi kullanıcı ile ilişkili buradan belirtiyoruz. User tablosu(modeli) ile OneToOne ilişki kuruldu.
    # on_delete=models.CASCADE
    
    def __str__(self):
        return self.user.username
        # bu user ait username görünsün demek
        
        
class Address(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #? relations burada belirtiliyor.
    
    def __str__(self):
        return "{} {}".format(self.name, self.city)
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User) #!on_delete burada yok, ManyToMany olduğundan
    
    def __str__(self):
        return self.name
        # return f"{self.name}"
        # return "{}".format(self.name)
    

#? on_delete properties:
    #* OneToOne
    #* OneToMany  bu ikisinde kullanılır,
    #! ManyToMany bunda kullanımaz,

'''
on_delete properties:
    # CASCADE -> if primary deleted, delete foreing too.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value')
    # DO_NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary.
'''

  
'''
on_delete properties: (Profile içinde user'a verildi yukarıda)
    # CASCADE -> if primary deleted, delete foreing too. (user silince ona ait profile/address de sil)
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True kullanmak gerekiyor) (user silinse bile profile bilgisi kalsın istersek kullanılır ve null atar)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value') (mesela anynomous verilir default, user silinince anynomous user olarak kalır.)
    # DO_NOTHING -> if primary deleted, do nothing. (birşey yapma, user silinse bile bütün profile bilgisi kalsın demek)
    # PROTECT -> if foreign is exist, can not delete primary. (user'ın silinmesine izin verme, başka tablolara bağlı vs'den dolayı)
'''

#! -------------------------------------------------------------------
#! -------------------  Models Relations Dj03 ------------------------
#! -------------------------------------------------------------------

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




#? shell ile sorgu komut örnekleri;
# python manage.py shell (önce shell terminali aç)
# from fscohort.models import Student (sonra sorgu yapılacak modeli import et)
# https://docs.djangoproject.com/en/4.1/topics/db/queries/

# s1 = Student(first_name='aaaa',last_name='a', number=4)
# s1.save()
# s1.first_name=bbbb
# s1.save()
# s2 = Student.objects.create(first_name='cccc', last_name='c', number=5)
# student = Student.objects.all()
# print(student.query)
# for s in student: print(s)
# s1 = Student.objects.get(number=2)
# s1.number=1
# s1.save()
# s1 = Student.objects.get(number=1) errorrr
# s1 = Student.objects.filter(number=1)
# s1 = Student.objects.exclude(number=1)
# s1 = Student.objects.get(first_name__exact='Henry')
# s1 = Student.objects.get(first_name__exact='Henry')
# s1 = Student.objects.get(first_name__iexact='henry')
# s1 = Student.objects.get(last_name__contains='v')
# s1 = Student.objects.get(last_name__startswith='v')
# s1 = Student.objects.filter(number__gt=1)