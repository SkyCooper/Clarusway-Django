from django.urls import path
from rest_framework import routers
from .views import ReservationMVS, CarMVS
from .views import ReservationView, ReservationDetailView
router = routers.DefaultRouter()
router.register("car", CarMVS)
# router.register("reservation", ReservationMVS)

urlpatterns = [
    path('reservation/', ReservationView.as_view()),
    path('reservation/<int:pk>/', ReservationDetailView.as_view())
]

urlpatterns += router.urls
