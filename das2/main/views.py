from django.shortcuts import render, redirect
from .forms import ContactModelForm
from .models import Contact
# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def mas_1(request):
    mylist = request.POST.get('mylist')
    res = []
    if not mylist:
        res = []
    else:
        try:
            mylist = mylist.split(' ')
            for i in mylist:
                if int(i) %2 == 0:
                    res.append(int(i))
        except:
            res = 'Eror 404'

    return render(request, 'main/mas_1.html', context={'res':res})


def mas_2(request):
    fact = request.POST.get('fact')
    res = 1
    if not fact:
        res = 0
    elif int(fact) < 0:
        res = 'Number is negative'
    else:
        try:
            for i in range(1, int(fact)+1):
                res *= i
        except:
            res = 'Eror 404'
    return render(request, 'main/mas_2.html', context={'res':res})


def mas_3(request):
    list1 = request.POST.get('list1')
    list2 = request.POST.get('list2')
    list3 = []
    if not list1 or not list2:
        list3 = []
    else:
        list1 = list1.split(' ')
        list2 = list2.split(' ')
        try:
            for i,j in zip(list1, list2):
                if int(i) > int(j):
                    list3.append(int(i))
                else:
                    list3.append(int(j))
        except:
            list3 = 'Eror 404'


    return render(request, 'main/mas_3.html', context={'list3':list3})


def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('contact')
        else:
            form = ContactModelForm()
    return render(request, 'main/contact_us.html')


