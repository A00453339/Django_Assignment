from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotels
from .serializers import HotelSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

def home(request):
    return HttpResponse("<h1> Hello Canada </h1>")


@api_view(['GET', 'POST'])
def hotel_details(request):
    if request.method == "GET":
        hotel_list = Hotels.objects.all()
        hotel_get_serializer =HotelSerializers(hotel_list, many=True)
        return Response(hotel_get_serializer.data)
    if request.method == "POST":
        hotel_val = request.data
        hotel_post_serializer = HotelSerializers(data=hotel_val)
        if hotel_post_serializer.is_valid():
            hotel_post_serializer.save()
        return Response({"Message": "Added Successfully"})


@api_view(['GET'])
def hotel_filters(request, pk):
    if request.method == "GET":
        hotel_list = Hotels.objects.get(id=pk)
        hotel_get_serializer = HotelSerializers(hotel_list, many=False)
        return Response(hotel_get_serializer.data)

