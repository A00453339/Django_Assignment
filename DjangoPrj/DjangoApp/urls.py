from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("hotel_list/", views.hotel_details, name="hotel_list"),
    path("hotel_list/<str:pk>", views.hotel_filters, name="hotel_filter")

]