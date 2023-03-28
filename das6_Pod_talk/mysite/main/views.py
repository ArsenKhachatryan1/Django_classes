from django.shortcuts import render, redirect
from . models import Hero, Topic, Download, Social, Contact
from .forms import ContactForm
from django.db.models import Q
# Create your views here.


def index(request):
    hero_list = Hero.objects.all()
    topic_list = Topic.objects.all()
    download = Download.objects.all()
    social = Social.objects.all()
    search_post = request.GET.get('search')
    if search_post:    
        posts = Hero.objects.filter(Q(name__icontains=search_post))
    else:
        posts = Hero.objects.all()
    return render(request, 'main/index.html', context={
        'hero_list':hero_list,
        'topic_list':topic_list,
        'download':download,
        'social':social,
        'posts':posts,
        })




def about(request):
    download = Download.objects.all()
    social = Social.objects.all()
    return render(request, 'main/about.html', context={
        'download':download,
        'social':social,
        })


def listing_page(request):
    download = Download.objects.all()
    social = Social.objects.all()
    return render(request, 'main/listing-page.html', context={
        'download':download,
        'social':social,
        })


def detail_page(request):
    download = Download.objects.all()
    social = Social.objects.all()
    return render(request, 'main/detail-page.html', context={
        'download':download,
        'social':social,
        })



def contact(request):
    download = Download.objects.all()
    social = Social.objects.all()
    contact_us = Contact.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', context={
        'download':download,
        'social':social,
        'contact_us':contact_us,
        'form': form,
        })