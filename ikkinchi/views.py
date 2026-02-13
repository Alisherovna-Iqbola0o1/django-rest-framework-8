from django.shortcuts import render
from .models import Salom1, Salom2, Salom3, Salom4, Salom5
from .serializers import Salom1Serializer, Salom2Serializer, Salom3Serializer, Salom4Serializer, Salom5Serializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class Salom1ListCreateAPIView(ListCreateAPIView):
    serializer_class = Salom1Serializer
    queryset = Salom1.objects.all()

class Salom2ListCreateAPIView(ListCreateAPIView):
    serializer_class = Salom2Serializer
    queryset = Salom2.objects.all()

class Salom3ListCreateAPIView(ListCreateAPIView):
    serializer_class = Salom3Serializer
    queryset = Salom3.objects.all()

class Salom4ListCreateAPIView(ListCreateAPIView):
    serializer_class = Salom4Serializer
    queryset = Salom4.objects.all()

class Salom5ListCreateAPIView(ListCreateAPIView):
    serializer_class = Salom5Serializer
    queryset = Salom5.objects.all()