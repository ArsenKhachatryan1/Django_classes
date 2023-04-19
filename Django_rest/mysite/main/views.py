from django.shortcuts import render
from . models import Phone, Nout
from .serializers import PhoneSerializer, NoutSerializer
from rest_framework import viewsets
# Create your views here.



class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class NoutViewSet(viewsets.ModelViewSet):
    queryset = Nout.objects.all()
    serializer_class = NoutSerializer