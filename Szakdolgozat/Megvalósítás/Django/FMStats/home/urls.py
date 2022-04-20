from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
   # path('',views.home, name='home'),
    #path('add',views.add, name='index')
    path('',views.home, name='home'),
    path(r'^clubwithchosen/(?P<chosenclub>)/$',views.clubwithchosen, name='clubwithchosen'),
    path('club',views.club, name='club')
    
]