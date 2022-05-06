from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
   # path('',views.home, name='home'),
    #path('add',views.add, name='index')
    path('',views.home, name='home'),
    path(r'^clubwithchosen/(?P<chosenclub>)/$',views.clubwithchosen, name='clubwithchosen'),
    path(r'^foundedplayers/(?P<playerid>)/$',views.foundedplayers, name='foundedplayers'),
    path('findSimilarPlayersMode',views.findSimilarPlayersMode, name='findSimilarPlayersMode'),
    path('club',views.club, name='club')
    
]