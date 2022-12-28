from rest_framework import serializers
from .models import Student, Path


class StudentSerializer(serializers.ModelSerializer):
    
    # born_year = serializers.SerializerMethodField()  # read_only
    path = serializers.StringRelatedField() # read_only
    path_id = serializers.IntegerField()
    
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ["id","first_name", "last_name","number", "path", "path_id"]
        # exclude = ["number"]
        
    
    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    
    
class PathSerializer(serializers.ModelSerializer):
    
    students = StudentSerializer(many=True)
    # students = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='detail'
    # )
    
    class Meta:
        model = Path
        # fields = "__all__"
        fields = ["id", "path_name", "students"]