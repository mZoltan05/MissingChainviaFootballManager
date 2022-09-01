from home.Logic import Logic

class StartTest():

    def TestColumnVisibilitiesInit_AllColumnsAreFalse(self):
        column_visibilities = {'name': False, 'club': False, 'age': False, 'born': False, 'height': False, 'weight': False, 'bestpos': False, 'nation': False, 'preferredfoot': False, 'value': False, 'wage': False, 'gk_properties': False, 'technical_properties': False, 'mental_properties': False, 'physical_properties_1': False, 'physical_properties_2': False, 'position_properties': False}
        Logic.ColumnVisibilitiesInit(column_visibilities)
        for column in column_visibilities:
            assert column_visibilities[column] == True ,"TestColumnVisibilitiesInit_AllColumnsAreFalse says: "+str(column)+"'s visibility should be True"
        
    def TestColumnVisibilitiesInit_NotAllColumnsAreFalse(self):
        column_visibilities = {'name': False, 'club': True, 'age': False, 'born': False, 'height': False, 'weight': False, 'bestpos': False, 'nation': False, 'preferredfoot': False, 'value': False, 'wage': False, 'gk_properties': False, 'technical_properties': False, 'mental_properties': False, 'physical_properties_1': False, 'physical_properties_2': False, 'position_properties': False}
        Logic.ColumnVisibilitiesInit(column_visibilities)
        allColumnsAreFalse = True
        for column in column_visibilities:
            if column_visibilities[column] == False:
                allColumnsAreFalse = False
                break
        assert allColumnsAreFalse == False ,"TestColumnVisibilitiesInit_NotAllColumnsAreFalse says: All columns's visibility are True"

    def TestCreateOrderByString(self):
        orderbyList = {'orderby1': ['Magasság', 'asc'], 'orderby2': ['Kor', 'asc'], 'orderby3': ['', 'asc'], 'orderby4': ['Érték', 'desc'], 'orderby5': ['', 'asc']}
        orderByString = Logic.CreateOrderByString(orderbyList)
        predictedorderByString = "ORDER BY  Height asc,  Age asc,  Value desc"
        assert orderByString == predictedorderByString, "TestCreateOrderByString says: OrderbyString won't work!"


        
    def test(self):
        try:
            self.TestColumnVisibilitiesInit_AllColumnsAreFalse()
            self.TestColumnVisibilitiesInit_NotAllColumnsAreFalse()
            self.TestCreateOrderByString()


            print()
            print("----  TEST OK  ----")
            print()
        except Exception as e:
            print("****************************************")
            print("********",e)
            print("****************************************")

    