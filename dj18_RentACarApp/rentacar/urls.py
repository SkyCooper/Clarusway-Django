from django.urls import path
from rest_framework import routers
from .views import ReservationMVS, CarMVS

router = routers.DefaultRouter()
router.register("car", CarMVS)
router.register("reservation", ReservationMVS)

urlpatterns = router.urls
