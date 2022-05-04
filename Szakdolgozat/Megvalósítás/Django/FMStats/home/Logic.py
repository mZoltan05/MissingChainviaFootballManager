from home.models import Player, Score

class Logic:
    
    def CreateOrderByString(orderByList):
        orderByString = ''
        for column in orderByList:
            if orderByList[column] != '' and ( orderByList[column][0] in [f.name for f in Player._meta.get_fields()] or  orderByList[column][0] in [f.name for f in Score._meta.get_fields()] or orderByList[column][0] in ['Súly','Kor','Magasság','Érték','Fizetés']):
                if orderByList[column][0] == 'Súly':
                    orderByString += ' Weight ' + orderByList[column][1] + ', '
                elif orderByList[column][0] == 'Kor':
                    orderByString += ' Age ' + orderByList[column][1] + ', '
                elif orderByList[column][0] == 'Magasság':
                    orderByString += ' Height ' + orderByList[column][1] + ', '
                elif orderByList[column][0] == 'Érték':
                    orderByString += ' Value ' + orderByList[column][1] + ', '
                elif orderByList[column][0] == 'Fizetés':
                    orderByString += ' Wage ' + orderByList[column][1] + ', '
                else:
                    orderByString += orderByList[column][0]+' ' + orderByList[column][1] + ', '
        if orderByString != '':
            orderByString = ' ORDER BY ' + orderByString[0:-2]
        return orderByString


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
        orderByList = {'orderby1':['',''],'orderby2':['',''],'orderby3':['',''],'orderby4':['',''],'orderby5':['','']}
        
        for i in range(1,6):
            try:
                orderByList['orderby'+str(i)][0] = request.GET['orderby'+str(i)]
            except:
                pass
            try:
                if request.GET['desc'+str(i)] == 'on':
                    orderByList['orderby'+str(i)][1] = 'desc'
            except:
                orderByList['orderby'+str(i)][1] = 'asc'
        return orderByList
