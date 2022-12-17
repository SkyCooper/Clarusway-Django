import os
os.system('cls' if os.name == 'nt' else 'clear')

# terminalde çıktı ekranında kod kalabalığı olmasını önler,

print("--------------------------------")

#! Topics to be Covered:
#* Everything in Python is class
#* Defining class
#* Defining class attributes
#* Difference between class attributes and instance attributes
#* SELF keyword
#* Defining methods
#* Class Methods vs. Static Methods and Instance Methods
#* Special methods (init, str)
#* 4 pillars of OOP:
    #? Encapsulation
    #? Abstraction
    #? Inheritance
        #? Multiple inheritance
    #? Polymorphism
        #? Overriding methods
#* Inner class
#* extra subjects


#! What is OOP?
""" 
# Object Oriented programming (OOP) is a programming paradigm that relies on the concept of classes and objects.
# It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects.
# significantly reduces code repetition by classifying similar structures (dont repeat yourself)
# Easier to debug, classes often contain all applicable information to them
# Secure, protects information through encapsulation 

"""


#! Everything in Python is class
""" 
# Python >generally class based  vs.  javascript >generally function based
def print_types(data):
    for i in data:
        print(i, type(i))
        
test = [122, "victor", [1, 2, 3], (1,2,3), {1,2,3}, True, lambda x:x]

print_types(test)

"""

#! defining class:
#* Class oluştururken isimlendirmede PascalCase yapı kullanılır. (Her kelimenin ilk harfi büyük ve bitişik.)
# "class" keyword for defining 
# There is a convention among languages that the class name should be capitalized.

"""

class Person:
  name = "cooper" # class attrinutes/properties
  age = 41


#* Classlardan türetilmiş objelere "instance" denir.  

person1 = Person() # creating object or instance
person2 = Person()

print(person1.name, "person1") # instances inherites class atributes
print(person2.age, "person2")

Person.job = "developer" #* yeni bir attribute eklendi kalıba, yani klasa
print(person1.job) # there is connection between classes and insttances

"""

#! class attributes vs instance attributes

""" 
#* Class içinde tanımlanmış değişkenlere "attribute veya property", fonksiyonlara "method" denir. Fonksiyonlarda atanmış değişkenlere "argument veya parameter" denir.

class Person:
  company = "clarusway"

person1 = Person() 
person2 = Person()

person1.location = "Turkey"
person1.company = "Tesla"
print(person1.location)
# print(person2.location) olmadığı için hata verir
print(person1.company) # Tesla (önce instance person1, sonra classa Person bakılır.)
print(person2.company) # Clarusway


Person.company = "Microsoft"  # Class değişti ama önce instance bakılır.
print(person1.company) # Tesla (önce instance person1, sonra classa Person bakılır.)
print(person2.company) # Microsoft,  olur.

"""

#! SELF keyword and methods

"""

class Person:
  company = "clarusway"
  
  def test():   # burada yazılan fonksiyon bu classın bir metodudur. 
                # boş olursa hata verir
    print("test")
    
#? "self" parametresini JS'deki "this" ile bağdaştırabilirsiniz. Fark: JS'deki "this" otomatik olarak her yerdedir, ama Python'daki "self" parametre olarak gönderilmelidir.
    
  def deneme(self): # herhangi bir isim versek olur bestpractice self yazılır.
    print("deneme")
    
#? JS'deki "setter" ve "getter" methodları, pythonda da mevcuttur.
#? get_method_name(self):
#? set_method_name(self, parameters):

  def set_details(self, name, age):
      self.name = name
      self.age = age
    
  def get_details(self):
    print(f"{self.name} - {self.age}")
  
  #! instance göre değişmeyen static metod, self parametresi yazmaya gerek yok.
  @staticmethod   #*bu keyword kullanmak gerekli.  
  def salute():
    print("Hi there!")



person1 = Person() 
person2 = Person()
person3 = Person()

# person1.test() #* TypeError hatası verir.
# Person.test(person1) arka planda python böyle çalıştığından hata veriyor.
# self --> çalıştırılan instance temsil eder.

person1.deneme()

person1.name = "cooper"
person1.age = 41

person1.get_details()
# person2.get_details() hata verir çünkü name/age person2 de yok.

person2.name = "victor"
person2.age = 33
person2.get_details() # hata verirmez artık, çünkü name/age person2 ye atandı.

#! set ederek attribute ekleme;
person3.set_details("karaMurat", 39)
person3.get_details()

person1.salute()  # static method olduğundan hata vermeden çalışır.

"""

#! special methods (dunder methods' da deniyor.)

""" 
#* Python'da özel methodlara (önceden tanımlanmış metodlar) "dunder" (double underscore) methodlar denir.

class Person:
  company = "clarusway"
  
  def set_details(self, name, age):
    self.name = name
    self.age = age
    
  def get_details(self):
    print(f"{self.name} - {self.age}")
  
person1 = Person()

person1.name = "victor"
person1.age = 33

person1.set_details("cooper", 41)
person1.get_details()


#! init metodu;
class Person2:
  company = "clarusway"
  count = 0
  
  def __init__(self, name, age, gender="male"):
    self.name = name
    self.age = age
    self.gender = gender
    Person2.count += 1 # her instance create edildiğinde init medotu çalışacağı için bu şekilde sayısını tutabiliriz.
    
  def __str__(self):
    return f"{self.name} - {self.age}"
    
  def get_details(self):
    print(f"{self.name} - {self.age}- {self.gender}")

# person2 = Person2() init olduğu için boş olursa hata verir.
# fakat gender default tanımlandığı için yazılmasa tanımlanan değeri alır.
person2 = Person2("victor", 33)
person2.get_details()

person3 = Person2("helen", 30, "female")
person3.get_details()
print(Person2.count) # person2 ve person3 oluştuğundan çıktısı 2 olur.


#! __str__ metodu;
# This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object. This method must return the String object.

print(person2)
print(person3)

"""


#!  OOP Princaples (4 pillars) :
    #* Encapsulation
    #* Abstraction
    #* Inheritance
    #* Polymorphism
    
        
#? Encapsulation (Kapsülleme)
""" 
# izinsiz girişleri ve değiştirmeleri engelleme (python da tam olarak uygulaması yoktur.)
  
# The princible in which we determine how much of the classes, data and methods can be viewed and how much can be changed by the user.

# kullanıcı tarafından sınıfların, verilerin ve metodların ne kadarının görüntülenebileceğini, ne kadarının değiştirilebileceğini belirlendiğimiz yapı

  # public - private - protected (not in python or js)
  # there is not a complete encapsulation in python
  
class Person:
  company = "clarusway"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self._id = 5000 # başına_ koyunca private oldu
    #! değiştirilebilir ama bunu değiştirirsen sıkıntı çıkar demektir.
    self.__number = 200

    
  def __str__(self):
    return f"{self.name} - {self.age}"
    
  def get_details(self):
    print(f"{self.name} - {self.age}- {self.gender}")


person1 = Person("cooper", 41)  
print(person1._id) # _ olursa ulaşılır
# print(person1.__number) # __ olursa daha koruyucu, ulaşılmaz
print(person1._Person__number) #* böyle ulaşılır, kesin bir kapsülleme yok.

"""  
  
  
#? Abstraction (Soyutlama)
"""

# Abstraction is the process of hiding the internal complex details of an application from the outer world. Abstraction is used to describe things in simple terms. It's used to create a boundary between the application and the client programs.  

# kullanıcı gereksiz detaylardan ve bilmesine ihtiyaç olmayan yapıdan uzaklaştırarak yormamak - soyutlama

# user bilmesin ben bileyim yeter gibi, kahve makinesi gibi, içinde nasıl yapıyor önemli değil, kahve yaptığını bilmek yeter.

# Abstraction, bir nesnenin önemli olan özelliklerini ve davranışlarını ortaya çıkarma işlemidir. Bu sayede nesnenin detayları gizlenir ve sadece temel özellikleri ve davranışları kullanıcılar tarafından görülebilir. Bu sayede nesneler daha basit ve kolay anlaşılır hale gelir. Abstraction, encapsulation ile birlikte kullanılarak kodun daha anlaşılır ve değiştirilebilir hale gelmesine yardımcı olur.

mylist= [2,3,5,1,4]
mylist.sort()
print(mylist)

# mesela listeyi sort etti ama nasıl eeti , arka planda ne yaptı bizim için çok da önemli değil, gereksiz bir sürü detay...

"""


#? Inheritance
    #? Multiple inheritance 
    


# * inheritance   => kalıtım. Parent'tan chield'a aktarılması        
        
class Person:
  company = "clarusway"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f"{self.name} - {self.age}"
    
  def get_details(self):
    print(f"{self.name} - {self.age}")
    

class Lang:
  def __init__(self, langs):
    self.langs = langs
    
  def display_langs(self):
    print(self.langs)     
        
#! Persondan yeni class oluşturma;
#* class keywordu ve () içine miras alındığı class yazılır.

class Employee123(Person):
  pass # Person clasının birebir aynısı bir class oluşturur.
  # pass # burada indentation'dan dolayı pass yazmazsak hata verir. geç birşey yapma demek

class Employee(Person, Lang):
#* hem person hemde Lang clasınından miraz alır,
#* super() komutu, inherit edilen İLK parent classı temsil eder.
  
  def __init__(self, name, age, path, langs):
    # self.name = name #! override ederken tekrar aynılarını yazmaya gerek yok, super kullan
    # self.age = age
    super().__init__(name, age) #!bir üst parentten al, değiştirme demek
    #! super() kullanınca self parametresine gerek kalmaz ve ilk parenti temsil ettiğimizi belirtir.
    Lang.__init__(self, langs) #* tekrar super kullanılmaz, Class ismi yazılır.
    self.path = path # Personda olmayan bir özellik ekledik, owerrite ettik.

  def get_details(self):
    # print(f"{self.name} - {self.age} - {self.path}") #* böyle tek tek yazılır veya super kullanılır.
    super().get_details() #! parentin aynısını al
    print(self.path) #! sonra eklenen path'de ayrıca çıktı al
    return super().get_details()



emp1 = Employee("barry", 20, "FS", "Python")        
emp1.get_details()
emp1.display_langs()
print(emp1.company) #clasurway        
        
      
    

      
#? Polymorphism
  #? Overriding methods
#* overriding = parent'tan gelen yapı ihtiyacımızı tam karşılamıyorsa update edebilmemiz.

#* overloading = parent'tan gelen yapıyı farklı parametrelerle değiştirebilmemiz. veya methodu birden farklı tanımlayabilmemizdir. Verilen parametlere göre kendisi seçerek kullanır.
  # Python overloading modelini desteklemez. Bunu, ekstra moduller ile gerçekleştirebilirsiniz.
  
  
  
  
#? Other Topics (Bonus)

print(Employee.mro()) #mro => Method resolution order: #! Kalıtım zinciri demek

print(help(Employee)) #! clasın bütün özelliklerini yazdırır.
#? terminalde help'ten çıkmak için :q yapmak lazım..

print(emp1.__dict__) # bu instancen özelliklerine bakmak için

print(isinstance(emp1, Employee)) # True / False çıktı verir. --> True

print(issubclass(Lang, Person)) # True / False çıktı verir. ---> False 


#! getattr(instance, attribute) : returns attribute value of instance
#! setattr(instance, attribute, new value) : update attribute of instance
#! hasattr(instance, attribute) : return boolean
#! delattr(instance, attribute) : delete attribute of instance

print(getattr(emp1, "name")) #  emp1 instancenın name attrubute
x = getattr(emp1, "name")  #  emp1 instancenın name attrubute bir değişkene atanması
print(x)

setattr(emp1,"name", "cooper")
print(getattr(emp1, "name"))

print(hasattr(emp1, "name"))

delattr(emp1, "age")
print(emp1.__dict__) # artık age yok, silindi.


#? inner class;

from django.db import models

class Makale(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "makaleler"











print("---------------------------------")