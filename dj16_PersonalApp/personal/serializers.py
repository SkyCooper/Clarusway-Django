from rest_framework import serializers
from .models import Department, Personal

from django.utils.timezone import now

class DepartmentSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = ("id", "name", "personal_count")
        
    def get_personal_count(self, obj):
        return obj.personals.count()
        
class PersonalSerializer(serializers.ModelSerializer):
    create_user_id = serializers.IntegerField(required=False)
    create_user = serializers.StringRelatedField()
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = Personal
        fields = "__all__"
    
    #? aynı işemi view tarafında yaptığımız için yoruma aldık,    
    # def create(self, validated_data):
    #     validated_data["create_user_id"] = self.context["request"].user.id
    #     return super().create(validated_data)
    
        # veya;
        # instance = Personal.objects.create(**validated_data)
        # return instance
        
    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days
        
        # import datetime
        # current_time = datetime.datetime.now()
        # return current_time.day - obj.start_date.day

class DepartmentDynamicSerializer(serializers.ModelSerializer):
  personals = PersonalSerializer(many=True, required=False)
  personal_count = serializers.SerializerMethodField()
  id = serializers.StringRelatedField()
  
  class Meta:
    model = Department
    fields = ("id", "name", "personal_count", "personals")
    
  def get_personal_count(self, obj):
    return obj.personals.count()