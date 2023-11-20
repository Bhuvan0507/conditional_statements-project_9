from django.shortcuts import render

# Create your views here.

def conditions(request):

    D={'a':1000, 'b':5000, 'c':7000}


    return render(request,'conditions.html',context=D)