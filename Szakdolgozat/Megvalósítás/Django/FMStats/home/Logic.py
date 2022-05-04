from home.models import Player, Score

class Logic:
    
    def CreateOrderByString(orderByList):
        orderByString = ''
        for column in orderByList:
            if orderByList[column] != '' and column != 'asc' and ( orderByList[column] in [f.name for f in Player._meta.get_fields()] or  orderByList[column] in [f.name for f in Score._meta.get_fields()] or orderByList[column] in ['Súly','Kor','Magasság','Érték','Fizetés']):
                if orderByList[column] == 'Súly':
                    orderByString += ' Weight, '
                elif orderByList[column] == 'Kor':
                    orderByString += ' Age, '
                elif orderByList[column] == 'Magasság':
                    orderByString += ' Height, '
                elif orderByList[column] == 'Érték':
                    orderByString += ' Value, '
                elif orderByList[column] == 'Fizetés':
                    orderByString += ' Wage, '
                else:
                    orderByString += orderByList[column] +', '
        if orderByString != '':
            orderByString = ' ORDER BY ' + orderByString[0:-2] + ' ' + orderByList['asc']
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
