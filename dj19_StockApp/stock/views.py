from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class BrandMVS(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    

class FirmMVS(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    

class ProductMVS(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    

class PurchasesMVS(ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        purchase = serializer.save()
        purchase.price_total = purchase.quantity * purchase.price
        purchase.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class SalesMVS(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        sale = serializer.save()
        sale.price_total = sale.quantity * sale.price
        sale.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
