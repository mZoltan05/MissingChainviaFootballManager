from http.client import SWITCHING_PROTOCOLS
from pickle import FALSE
from traceback import format_exc
from urllib import request
from django.forms import formset_factory
from django.shortcuts import render
from home.models import Club
from home.PlayersInstance import PlayersInstance
from home.Logic import Logic
# Create your views here.

def home(request):
    
    instance = PlayersInstance(request)
    players = instance.GetPlayers()
    #print(Club._meta.get_fields())
    #print([f.name for f in Club._meta.get_fields()])
    return(render(request,'home.html',{'players':players,'column_visibilities':instance.column_visibilities,'text_searches':instance.text_searches,'int_searches_bottom':instance.int_searches_bottom,'int_searches_top':instance.int_searches_top,'orderbylist':instance.orderByList}))

def clubwithchosen(request,chosenclub):
    text_searches = {'name_txt':chosenclub}
    query = "SELECT * FROM club WHERE 1=1 AND name LIKE '%%"+chosenclub+"%%'" # + wherestring + " limit 500"
    clubs = Club.objects.raw(query)
    return(render(request,'club.html',{'clubs':clubs,'text_searches':text_searches}))


def club(request):
    text_searches = {'name_txt':'','division_txt':'','based_txt':''}
    wherestring = Logic.CreateWhereString(request,text_searches,{},{})
    #print(wherestring)
    query = "SELECT * FROM club WHERE 1=1 " + wherestring #limit 500"
    clubs = Club.objects.raw(query)
    return(render(request,'club.html',{'clubs':clubs,'text_searches':text_searches}))

