from typing import get_args
from django.http import HttpResponse
from django.shortcuts import render

#from calc.models import People
# Create your views here.

#def home (request):
#    peoples = People.objects.all()
#    return render(request, 'home.html',{'people':peoples})

def players(request):
    return(render(request,'players.html'))