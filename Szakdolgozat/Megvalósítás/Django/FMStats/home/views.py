from http.client import SWITCHING_PROTOCOLS
from pickle import FALSE
from traceback import format_exc
from urllib import request
from django.forms import formset_factory
from django.shortcuts import render
from home.models import Club
from home.models import Player
# Create your views here.

def home(request):
    
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
        'wage':CheckBoxValueToBoolean(request, 'wage'),

        'gk_properties':CheckBoxValueToBoolean(request, 'gk_properties'),
        'technical_properties':CheckBoxValueToBoolean(request, 'technical_properties'),
        'mental_properties':CheckBoxValueToBoolean(request, 'mental_properties'),
        'physical_properties_1':CheckBoxValueToBoolean(request, 'physical_properties_1'),
        'physical_properties_2':CheckBoxValueToBoolean(request, 'physical_properties_2'),
        'position_properties':CheckBoxValueToBoolean(request, 'position_properties')
    }
    ColumnVisibilitiesInit(column_visibilities)

    text_searches = {'name_txt':'','club_txt':'','born_date':'','bestpos_txt':'','nation_txt':'','preferredfoot_txt':''}
    int_searches_bottom = {'age_bottom':'','height_bottom':'','weight_bottom':'','value_bottom':'','wage_bottom':''}
    int_searches_top = {'age_top':'','height_top':'','weight_top':'','weight_top':'','value_top':'','wage_top':''}

    

    orderByList = CreateOrderByList(request)
    orderByString = CreateOrderByString(orderByList)
    
    wherestring = CreateWhereString(request, text_searches, int_searches_bottom, int_searches_top)

    query = "SELECT * FROM player WHERE 1=1 "+ wherestring + orderByString + " limit 200"
    #print(query)
    players = Player.objects.raw(query)
    
    return(render(request,'home.html',{'players':players,'column_visibilities':column_visibilities,'text_searches':text_searches,'int_searches_bottom':int_searches_bottom,'int_searches_top':int_searches_top,'orderbylist':orderByList}))

def clubwithchosen(request,chosenclub):
    text_searches = {'name_txt':chosenclub}
    query = "SELECT * FROM club WHERE 1=1 AND name LIKE '%%"+chosenclub+"%%'" # + wherestring + " limit 500"
    clubs = Club.objects.raw(query)
    return(render(request,'club.html',{'clubs':clubs,'text_searches':text_searches}))


def club(request):
    text_searches = {'name_txt':'','division_txt':'','based_txt':''}
    wherestring = CreateWhereString(request,text_searches,{},{})
    #print(wherestring)
    query = "SELECT * FROM club WHERE 1=1 " + wherestring #limit 500"
    clubs = Club.objects.raw(query)
    return(render(request,'club.html',{'clubs':clubs,'text_searches':text_searches}))







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


def CreateWhereString(request, text_searches, int_searches_bottom, int_searches_top):
    wherestring = ""
    for search in text_searches:
        #print(search)
        try:
            value = request.GET[search]
            if search in ['bestpos_txt','nation_txt']:
                value = value.upper()
            if search in ['name_txt','club_txt','preferredfoot_txt','division_txt','based_txt']:
                value = value[0].upper() + value [1::1]
            if len(value) > 0:
              wherestring += " AND " + search.split('_')[0] + " LIKE '%%" + value + "%%'"
            text_searches[search] = value
        except:
          continue
    

    for search in int_searches_bottom:
        try:
            value = request.GET[search]
            if int(value) > -1:
              wherestring += " AND " + search.split('_')[0] + " > " + value
            int_searches_bottom[search] = value
        except:
          continue
    
    for search in int_searches_top:
        try:
            value = request.GET[search]
            if int(value) > -1:
              wherestring += " AND " + search.split('_')[0] + " < " + value
            int_searches_top[search] = value
        except:
          continue

    return wherestring


def CreateOrderByList(request):
    orderByList = {'orderby1':'','orderby2':'','orderby3':'','orderby4':'','orderby5':'','asc':''}
    
    try:
        orderByList['asc'] = request.GET['asc']
    except:
        orderByList['asc'] = 'asc'

    try:
        orderByList['orderby1'] = request.GET['orderby1']
    except:
        pass

    try:
        orderByList['orderby2'] = request.GET['orderby2']
    except:
        pass

    try:
        orderByList['orderby3'] = request.GET['orderby3']
    except:
        pass

    try:
        orderByList['orderby4'] = request.GET['orderby4']
    except:
        pass

    try:
        orderByList['orderby5'] = request.GET['orderby5']
    except:
        pass

    return orderByList


def CreateOrderByString(orderByList):
    orderByString = ''
    for column in orderByList:
        if orderByList[column] != '' and column != 'asc':
            if orderByList[column] == 'Súly':
                orderByString += ' Weight, '
            elif orderByList[column] == 'Kor':
                orderByString += ' Age, '
            elif orderByList[column] == 'Magasság':
                orderByString += ' Height, '
            elif orderByList[column] == 'Érték':
                orderByString += ' Value, '
            elif orderByList[column] == 'Fizetés':
                orderByString += ' Salary, '
            else:
                orderByString += orderByList[column] +', '
    if orderByString != '':
        orderByString = ' ORDER BY ' + orderByString[0:-2] + ' ' + orderByList['asc']
    return orderByString