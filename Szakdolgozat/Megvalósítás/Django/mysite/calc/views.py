from typing import get_args
from django.http import HttpResponse
from django.shortcuts import render

#from calc.models import People
from calc.models import Club
# Create your views here.

#def home (request):
#    peoples = People.objects.all()
#    return render(request, 'home.html',{'people':peoples})

def players(request):
    clubs = Club.objects.raw("SELECT * FROM club WHERE based like '%%England%%' ")
    print('--------------------------------------------------')
    print(clubs)
    print('--------------------------------------------------')
    return(render(request,'players.html',{'clubs':clubs}))
