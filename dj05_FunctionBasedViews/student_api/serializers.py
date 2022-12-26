from rest_framework import serializers
from .models import Student, Path

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
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


class StudentSerializer(serializers.ModelSerializer):
    
    born_year = serializers.SerializerMethodField()  # read_only
    path = serializers.StringRelatedField() # read_only
    path_id = serializers.IntegerField()
    
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ["id","first_name", "last_name","number", "age", "born_year", "path", "path_id"]
        # exclude = ["number"]
        
    
    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    
    
class PathSerializer(serializers.ModelSerializer):
    
    # students = StudentSerializer(many=True)
    students = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='detail'
    )
    
    class Meta:
        model = Path
        # fields = "__all__"
        fields = ["id", "path_name", "students"]