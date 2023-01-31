from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register("category", CategoryMVS)
router.register("brand", BrandMVS )
router.register("firm", FirmMVS )
router.register("product", ProductMVS )
router.register("purchases", PurchasesMVS )
router.register("sales", SalesMVS )

urlpatterns = router.urls