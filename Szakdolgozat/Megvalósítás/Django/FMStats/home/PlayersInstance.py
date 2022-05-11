from typing import OrderedDict
from home.Logic import Logic
from home.models import Player

class PlayersInstance:
    
    column_visibilities = {}
    text_searches = {}
    int_searches_bottom = {}
    int_searches_top = {}
    orderByList = []
    orderByString = ""
    wherestring = ""
    query = ""
    playerid = 0
    bestposForSearchUnderratedPlayers = ""

    def __init__(self,request):
        columns = ['name','club','age','born','height','weight','bestpos','nation','preferredfoot','value','wage','gk_properties','technical_properties','mental_properties','physical_properties_1','physical_properties_2','position_properties']
        for column in columns:
            self.column_visibilities[column] = Logic.CheckBoxValueToBoolean(request, column)

        Logic.ColumnVisibilitiesInit(self.column_visibilities)

        self.text_searches = {'name_txt':'','club_txt':'','born_date':'','bestpos_txt':'','nation_txt':'','preferredfoot_txt':''}
        self.int_searches_bottom = {'age_bottom':'','height_bottom':'','weight_bottom':'','value_bottom':'','wage_bottom':''}
        self.int_searches_top = {'age_top':'','height_top':'','weight_top':'','weight_top':'','value_top':'','wage_top':''}
        self.orderByList = Logic.CreateOrderByList(request)
        self.orderByString = Logic.CreateOrderByString(self.orderByList)

        
    def GetPlayers(self,request):

        print(self.query)
        self.wherestring = Logic.CreateWhereString(request,self.wherestring , self.text_searches, self.int_searches_bottom, self.int_searches_top)

        self.query = "SELECT * FROM player p inner join score_bak s ON CAST(p.playerid AS INT) = s.playerid WHERE 1=1 "+ self.wherestring + self.orderByString + " limit 200"

        return Player.objects.raw(self.query)