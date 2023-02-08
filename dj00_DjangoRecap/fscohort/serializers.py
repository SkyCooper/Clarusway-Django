from rest_framework import serializers
from .views import Student, Path

#? 1nci yöntem serializers'dan inherit
#? serializers'dan inherit edilirse create ve update metodlarınıda yazmak gerekli
#? model yapısındaki fieldType ların burada da aynı olması gerekiyor..

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=40)
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance


#? 2nci yöntem ModelSerializer;
#? ilave özellikleri; (web sitesinden)
# It will automatically generate a set of fields for you, based on the model.
# It will automatically generate validators for the serializer, such as unique_together validators.
# It includes simple default implementations of .create() and .update().

#? bu yukarıdakinin aynısını arka planda yapıyor,
class StudentSerializer(serializers.ModelSerializer):
    
    # yeni field ekleme;
    born_year = serializers.SerializerMethodField() #! SerializerMethodField => default -> read-only
    #* bunu fields = ["born_year"] içine eklememiz gerekli
    #! read-only ; yani sadece veri çekerken / okurken kullanılır.
    # create ederken / POST yaparken read-only olanlar kullanılmaz.
    # DB tablosunda olmayan veri ile create yapılamaz, born_year ve path kullanılamaz bundan dolayı.
    
    path = serializers.StringRelatedField() #!StringRelatedField => read-only
    #* bunu fields = ["path"] içine eklememiz gerekli
    # StringRelatedField eklenen path'ın id olarak değil ismen gelmesini sağlar.
    # Fakat öğrenci create ederken path ismini yazamayız. "aws, data, fs" bunu anlamaz (read-only olduğundan)
    # Çünkü db'de id var, id ile kayıt ekleyebilmek için path_id oluşturuyoruz,
    
    path_id = serializers.IntegerField()
    #* bunu fields = ["path_id"] içine eklememiz gerekli
    # Artık öğrenci create ederken path_id yazabiliriz.
    
    
    # Student model'den gelen fieldlar..
    class Meta:
        model = Student
        # fields = "__all__"
        #* "__all__" herşeyi dataya JSON olarak atar
        fields = ["id", "first_name", "last_name", "number", "age", "born_year", "path", "path_id"]
        #! bestpractice böyle kullanmak gerekli , ne istiyorsak onu yazıyoruz
        # fields = ["first_name", "last_name"]
        #* ["first_name", "last_name"] istediklerimizi dataya JSON olarak atar
        
        # exculue = ["number"]
        #* ["number"] hariç, kalan hepsini dataya JSON olarak atar
        
    #? yukarıda tanımlanan born_year başına get yazılıp kullanılır;
    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age    


class PathSerializer(serializers.ModelSerializer):
    
    # models.py'den alıntı: (anlamak için oraya bak)
    # yani child tabloda --> related_name='students' yazıyor olması  ;
    # students = ... (sanki böyle bir field varmış demektir.)
    # bundan dolayı burada students tanımlanabilir.
    
    students = StudentSerializer(many=True)
    #* StudentSerializer'den alınca postmen çıktısı çok kalabalık oluyor.
    
    # students = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='detail'
    # )
    #* HyperlinkedRelatedField'den alınca tek tek her öğrencinin endpoint name'ini verir.
    #! BURAYA DİKKAT ET !!!
    # urls içine --> name="detail" ekle yoksa hata verir.
    
    #* HyperlinkedRelatedField olursa postmen çıktısı;
    # {
    #     "id": 1,
    #     "path_name": "AWS",
    #     "students": [
    #         "http://127.0.0.1:8000/api/student/5",
    #         "http://127.0.0.1:8000/api/student/6",
    #         "http://127.0.0.1:8000/api/student/7",
    #         "http://127.0.0.1:8000/api/student/9"
    #     ]
    # },
    
    

    
    class Meta:
        model = Path
        # fields = "__all__"
        fields = ["id", "path_name", "students"]