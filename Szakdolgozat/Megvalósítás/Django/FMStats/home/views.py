from django.shortcuts import render
from home.models import Club
from home.models import Player
# Create your views here.

def home(request):
    players = Player.objects.raw("SELECT * FROM player ORDER BY weight desc  limit 1000 ")
    column_visibilities = {
        'name':True,
        'club':True,
        'age':True,
        'born':True,
        'height':True,
        'weight':True,
        'bestpos':True,
        'nation':True,
        'preferredfoot':True,
        'value':True,
        'wage':True
    }
    return(render(request,'home.html',{'players':players,'column_visibilities':column_visibilities}))
