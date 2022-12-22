from rest_framework import serializers
from .views import Student, Path

#? 1nci yöntem serializers'dan inherit
#? serializers'dan inherit edilirse create ve update metodlarınıda yazmak gerekli

# class StudentSerializer(serializers.Serializer):
#   first_name = serializers.CharField(max_length=30)
#   last_name = serializers.CharField(max_length=40)
#   number = serializers.IntegerField()
#   age = serializers.IntegerField()
  
#   def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#       instance.first_name = validated_data.get('first_name', instance.first_name)
#       instance.last_name = validated_data.get('last_name', instance.last_name)
#       instance.number = validated_data.get('number', instance.number)
#       instance.age = validated_data.get('age', instance.age)
#       instance.save()
#       return instance


#? 2nci yöntem ModelSerializer;
#? ilave özellikleri; (web sitesinden)
# It will automatically generate a set of fields for you, based on the model.
# It will automatically generate validators for the serializer, such as unique_together validators.
# It includes simple default implementations of .create() and .update().

#? bu yukarıdakinin aynısını arka planda yapıyor,
class StudentSerializer(serializers.ModelSerializer):
      
      # yeni field ekleme;
      born_year = serializers.SerializerMethodField() #! SerializerMethodField => read-only
      #* bunu fields = ["born_year"] içine eklememiz gerekli
      
      path = serializers.StringRelatedField() #!StringRelatedField => read-only
      #* StringRelatedField eklenen path'ın id olarak değil ismen gelmesini sağlar.
      #* Fakat öğrenci create ederken "aws, data, fs" bunu anlamaz
      #* bunu fields = ["path"] içine eklememiz gerekli
      
      path_id = serializers.IntegerField()
      #* bunu fields = ["path_id"] içine eklememiz gerekli
      
      
      # Student model'den gelen fieldlar..
      class Meta:
            model = Student
            # fields = "__all__"
            #* "__all__" herşeyi dataya JSON olarak atar
            fields = ["id", "first_name", "last_name", "number", "age","born_year", "path", "path_id"]
            # fields = ["first_name", "last_name"]
            #* ["first_name", "last_name"] istediklerimizi dataya JSON olarak atar
            # exculue = ["number"]
            #* ["number"] hariç, kalan hepsini dataya JSON olarak atar
      
      def get_born_year(self, obj):
            import datetime
            current_time = datetime.datetime.now()
            return current_time.year - obj.age    
      
class PathSerializer(serializers.ModelSerializer):
      class Meta:
            model = Path
            # fields = "__all__"
            fields = ["id", "path_name", "students"]