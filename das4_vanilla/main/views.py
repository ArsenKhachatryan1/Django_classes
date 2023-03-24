from django.shortcuts import render, redirect
from . models import Sitename, Portfolio, Story, Contact
from .forms import ContactForm
from .models import Contact
# Create your views here.

def index(request):
    sitename = Sitename.objects.all()[0]
    portfolio_list = Portfolio.objects.all()
    story_list = Story.objects.all()
    contact_us = Contact.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'main/index.html',
                   context={'sitename': sitename, 
                            'portfolio_list':portfolio_list,
                            'story_list':story_list,
                            'contact_us':contact_us,
                            'form': form
                            
                            }
                   )


