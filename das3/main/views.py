from django.shortcuts import render
from .models import Phone

# Create your views here.

def index(request):
    phone_list = Phone.objects.all()
    return render(request, 'main/index.html', context={
        'phone_list':phone_list})


def about(request):
    return render(request, 'main/about.html')
