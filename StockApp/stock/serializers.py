from rest_framework import serializers
from .models import *

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
        fields = "__all__"
        
#? gelen sorguda name varsa/yoksa ona göre farklı serializer kullanacak,        
#? CategorySerializer tekrar yazıp isim varsa product görünsün diye tekrar yazdık,    
class CategoryProductSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()  #read_only default
    c_products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ("id", "name", "product_count", "c_products")
    
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