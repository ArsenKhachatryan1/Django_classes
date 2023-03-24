from django.shortcuts import render
from .models import Phone
from django.db.models import Q

# Create your views here.

def index(request):
    search_post = request.GET.get('search')
    if search_post:    
        phone_list = Phone.objects.filter(Q(name__icontains=search_post) | Q(price__icontains=search_post))
    else:
        phone_list = Phone.objects.all()
    return render(request, 'main/index.html', context={
        'phone_list':phone_list})


def about(request):
    return render(request, 'main/about.html')


def index_detail(request, id):
    one_phone = Phone.objects.get(pk=id)
    return render(request, 'main/index_detail.html', context={
        'one_phone':one_phone})