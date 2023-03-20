from django.shortcuts import render

# Create your views here.
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class Category__ViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category__Serializer

class Products__ViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = Products__Serializer

class Users__ViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = Users__Serializer

class Orders__ViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = Orders__Serializer  


