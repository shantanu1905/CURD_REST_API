from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from main.serializers import StudentSerializer
from .models import *

# Create your views here.
class ListAPIView(ListAPIView):
    """This endpoint list all of the available Data from the database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CreateAPIView(CreateAPIView):
    """This endpoint allows for creation of a data and pull it over to database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific data by passing in the id of the data to update"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeleteAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific data from the database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer