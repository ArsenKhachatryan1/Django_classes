from django.shortcuts import render

# Create your views here.

def calculator(request):
    list1 = request.POST.get('list1')
    char = request.POST.get('char')
    list2 = request.POST.get('list2')
    list3 = []
    
    if not list1 or not list2:
        list3 = []
    else:
    
        list1 = list1.split(' ')
        list2 = list2.split(' ')

        if len(list1) != len(list2):
            list3.append('Input is not correct')
        else:
            for i,j in zip(list1,list2):
                if char == '+':
                    list3.append(int(i) + int(j))
                elif char == '-':
                    list3.append(int(i) - int(j))
                elif char == '*':
                    list3.append(int(i) * int(j))
                elif char == '/':
                    try:
                        list3.append(int(i) / int(j))
                    except ZeroDivisionError:
                        list3 = []
                    list3.append('Zero division')
                else:
                    list3.append('Wrong action')
                    break
    return render(request, 'calculator.html', context={'list3':list3})
