from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
        

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "image")
        
class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ("id", "name", "phone", "address", "image")
        

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    # brand = BrandSerializer()
    brand_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ("id", "name", "category", "category_id", "brand", "brand_id", "stock", "created_date", "updated_date")
        
class PurchasesSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    category = serializers.SerializerMethodField()
    class Meta:
        model = Purchases
        fields = ("id", "user", "firm", "product", "brand", "quantity", "price", "price_total","category")
        
    def get_category(self,obj):
        products = Product.objects.filter(id=obj.product_id).values()
        print(products)
        category_id= products[0]["category_id"]
        return list(Category.objects.filter(id=category_id).values())[0]["name"]
        
class SalesSerializer(serializers.ModelSerializer):
    # price_total = serializers.SerializerMethodField(method_name="total")
    class Meta:
        model = Sales
        fields = ("id", "user", "product", "brand", "quantity", "price", "price_total")
        
    # def total(self,obj):
    #     return obj.price * obj.quantity