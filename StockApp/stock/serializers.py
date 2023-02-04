from rest_framework import serializers
from .models import *

#! 1- Bütün kategorileri ve içindeki ürün sayılarını gösteren serializer
class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()  #read_only default
    class Meta:
        model = Category
        fields = ("id", "name", "product_count")
    
    def get_product_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count()
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = (
            "id",
            "name",
            "category",
            "category_id",
            "brand",
            "brand_id",
            "stock",
        )
        read_only_fields = ("stock",)
        
#! 2- sadece ilgili kategoriyi, ürün sayısını ve ÜRÜNLERİNİ gösteren serializer
#? gelen sorguda name varsa/yoksa ona göre farklı serializer kullanacak,        
#? CategorySerializer tekrar yazıp isim varsa product görünsün diye tekrar yazdık,    
class CategoryProductSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()  #read_only default
    
    #? burada yazılacak isim Product modeldeki category için tanımlanan related name ile aynı olacak,
    #? bir kagori içinde birden fazla product olacağından Many=True,
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ("id", "name", "product_count", "products")
    
    def get_product_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count()
        




class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "image")
        
class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ("id", "name", "phone", "address", "image")
        


        
class PurchasesSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField() 
    firm = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    
    class Meta:
        model = Purchases
        fields = (
            "id",
            "user",
            "user_id",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            "createds",
            "updated",
        )
class SalesSerializer(serializers.ModelSerializer):
    # price_total = serializers.SerializerMethodField(method_name="total")
    class Meta:
        model = Sales
        fields = ("id", "user", "product", "brand", "quantity", "price", "price_total")
        
    # def total(self,obj):
    #     return obj.price * obj.quantity