from urllib import request
from django.shortcuts import render
from home.models import Club
from home.models import Player
# Create your views here.

def home(request):
    
    wherestring = CreateWhereString()
    query = "SELECT * FROM player WHERE 1=1 "+ wherestring +" ORDER BY weight desc"
    players = Player.objects.raw(query)
    column_visibilities = {
        'name':CheckBoxValueToBoolean(request, 'name'),
        'club':CheckBoxValueToBoolean(request, 'club'),
        'age':CheckBoxValueToBoolean(request, 'age'),
        'born':CheckBoxValueToBoolean(request, 'born'),
        'height':CheckBoxValueToBoolean(request, 'height'),
        'weight':CheckBoxValueToBoolean(request, 'weight'),
        'bestpos':CheckBoxValueToBoolean(request, 'bestpos'),
        'nation':CheckBoxValueToBoolean(request, 'nation'),
        'preferredfoot':CheckBoxValueToBoolean(request, 'preferredfoot'),
        'value':CheckBoxValueToBoolean(request, 'value'),
        'wage':CheckBoxValueToBoolean(request, 'wage')
    }
    ColumnVisibilitiesInit(column_visibilities)

    return(render(request,'home.html',{'players':players,'column_visibilities':column_visibilities}))



def CheckBoxValueToBoolean(request, name):
    try:
        if request.GET[name] == 'on':
            return True
        else:
            return False
    except:
        return False

def ColumnVisibilitiesInit(column_visibilities):
    for column in column_visibilities:
        if column_visibilities[column] == True:
            return
    for column in column_visibilities:
        column_visibilities[column] = True
    return

def CreateWhereString():
    wherestring = "AND name like '%%Mark%%'" 
    return wherestring