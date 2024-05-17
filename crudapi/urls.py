from django.urls import path
from .views import *
urlpatterns = [
    path("", getAllCars),
    path("home/", getAllCars),
    path("addcar/", addcar),
    path("<int:car_id>/", detailcar),
    path("delete/<int:car_id>/", delete)
]