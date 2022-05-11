from django.shortcuts import render
from home.models import Club
from home.models import Player
from home.PlayersInstance import PlayersInstance
from home.Logic import Logic
import subprocess

def home(request):
    instance = PlayersInstance(request)
    players = instance.GetPlayers(request)
    instance.bestposForSearchUnderratedPlayers = ' '
    return(render(request,'home.html',{'players':players,'column_visibilities':instance.column_visibilities,'text_searches':instance.text_searches,'int_searches_bottom':instance.int_searches_bottom,'int_searches_top':instance.int_searches_top,'orderbylist':instance.orderByList,'bestposForSearchUnderratedPlayers':instance.bestposForSearchUnderratedPlayers}))

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


def foundedplayers(request,playerid):
    instance = PlayersInstance(request)
    subprocess_output = str(subprocess.run(["python", "..\..\ML\FindSimilarPlayer.py",playerid], capture_output=True).stdout)[3:-2]
    subprocess_output = "'"+subprocess_output.replace(", ","', '")+"'"
    print(subprocess_output)
    query = "SELECT * FROM player WHERE playerid in (" + subprocess_output+ " ) limit 100"
    players = Player.objects.raw(query)
    return(render(request,'home.html',{'players':players,'column_visibilities':instance.column_visibilities,'text_searches':instance.text_searches,'int_searches_bottom':instance.int_searches_bottom,'int_searches_top':instance.int_searches_top,'orderbylist':instance.orderByList,'isFindSimilarPlayersModeOn':True,'bestposForSearchUnderratedPlayers':instance.bestposForSearchUnderratedPlayers}))


def findSimilarPlayersMode(request):
    instance = PlayersInstance(request)
    players = instance.GetPlayers(request)
    return(render(request,'home.html',{'players':players,'column_visibilities':instance.column_visibilities,'text_searches':instance.text_searches,'int_searches_bottom':instance.int_searches_bottom,'int_searches_top':instance.int_searches_top,'orderbylist':instance.orderByList,'isFindSimilarPlayersModeOn':True,'bestposForSearchUnderratedPlayers':instance.bestposForSearchUnderratedPlayers}))

def findUnderratedPlayers(request):
    instance = PlayersInstance(request)
    try:
        instance.bestposForSearchUnderratedPlayers = request.GET['bestposForSearchUnderratedPlayers']
    except:
        instance.bestposForSearchUnderratedPlayers = ' '
    subprocess_output = str(subprocess.run(["python", "..\..\ML\FindUnderratedPlayersOnPosition.py",instance.bestposForSearchUnderratedPlayers], capture_output=True).stdout)[3:-2]
    subprocess_output = "'"+subprocess_output.replace(", ","', '")+"'"
    #query = "SELECT * FROM player WHERE playerid in (" + subprocess_output+ " ) limit 100"
    instance.wherestring = " AND p.playerid IN (" + subprocess_output+ " ) "
    players = instance.GetPlayers(request)
    #players = Player.objects.raw(query)
    return(render(request,'home.html',{'players':players,'column_visibilities':instance.column_visibilities,'text_searches':instance.text_searches,'int_searches_bottom':instance.int_searches_bottom,'int_searches_top':instance.int_searches_top,'orderbylist':instance.orderByList,'bestposForSearchUnderratedPlayers':instance.bestposForSearchUnderratedPlayers}))
