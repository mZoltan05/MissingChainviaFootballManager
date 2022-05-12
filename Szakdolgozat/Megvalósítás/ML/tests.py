import unittest

from sqlalchemy import create_engine
from Logic import Logic
import pandas as pd
from settings import Settings

class TestCompareList(unittest.TestCase):
    
    def test_compareList_EqualLists(self):
        list1 = [1, 2, 3, True, "List", 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.assertEqual(Logic.compareList(self, list1, list1), True)

    def test_compareList_NotEqualLists(self):
        list1 = [1, 2, 3, True, "List", 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        list2 = [1, 3, 0, True, "List", 4, 5, 6]
        self.assertEqual(Logic.compareList(self, list1, list2), False)
 

class TestFindSimilarPlayers(unittest.TestCase):

    
    def test_FindSimilarPlayers(self):
        
        alchemyEngine = create_engine(Settings.dbConString, pool_recycle=3600);
        dbConnection = alchemyEngine.connect();
        logic = Logic(dbConnection, 16170637)        

        testQuery = "SELECT playerid, striker, rightfoot, heading, acceleration, pace, temperament, pressure, dribbling, composure, firsttouch, agility, sportsmanship, finishing, decisions, leadership, leftfoot, loyalty, professional, offtheball, technique FROM score_bak WHERE playerid IN ( 1036117, 12034183, 13129199, 14026322, 1509925, 19190933, 23155553, 29166081, 37051983, 43207905, 50040310, 50049219, 50054166, 51010530, 51013515, 62146888, 65035985, 66037111, 67194152, 67197969, 64021612, 67198920, 65001396, 71012740, 65032169, 69000503, 71080578, 65033781, 7502199, 88020743, 98010752, 12034478, 13114995, 13175077, 15065345, 20020009, 23166485, 23168252, 24054185, 24055166, 39046277, 45035461, 53067786, 51000459, 519345, 51013588, 5790150, 59023732, 63029300, 65028834, 71029477, 65033355, 65033879, 75000320, 75007759, 75031278, 75041083, 7520894, 91121676, 88021822, 13118187, 14029265, 14140787, 20500614, 23309015, 38034240, 39030057, 49038461, 50054019, 51048339, 5754913, 62062431, 62073094, 62163728, 62181867, 65029938, 67097876, 65035942, 65010105, 662073, 75029706, 823542, 98029100, 12013183, 14063365, 19290873, 214751, 39045946, 38002386, 43117143, 51009959, 51017033, 13173476, 64004386, 65001706, 67190701, 67229616, 72048236, 91107790, 13103473, 155432, 23134375, 38017754, 42077615, 53019764, 76001462, 75033272, 81027694, 76036115, 83184994, 76037372, 85145121, 96092261, 96064085, 1042197, 14083029, 16189772, 17033354, 23128348, 37060912, 37061006, 38000365, 43079908, 42063634, 47045404, 48038951, 51030984, 51032489, 51042490, 51048140, 64004779, 65033655, 65030484, 67218662, 66032159, 69002679, 71086602, 77032093, 78000356, 91018969, 91019220, 91126250, 91155497, 1033176, 13104038, 13132714, 13171701, 14083096, 1507679, 23033705, 23309329, 25044547, 38039361, 41020366, 43039495, 43316138, 48036819, 51016199, 51031583, 51042387, 53115548, 5327562, 5760101, 5781791, 51063757, 65013707, 65013847, 65026327, 65035905, 65036816, 67245141, 67146858, 91124222, 92016696, 75020023, 98034885, 13167194, 14134249, 14146022, 14180408, 16004236, 1502398, 16155402, 15037629, 1650690, 19299087, 24047155, 23134174, 28091349, 42008935, 428298, 37056042, 43204005, 51013814, 51031032, 51047604, 62189035, 67118145, 67154584, 67022052, 75007270, 77046230, 78034703, 78047285, 7869415, 8507092, 93014072, 76022793, 96114728, 98000440, 15036579, 14120207, 20015295, 24052213, 24052447, 25003387, 24041532, 23248118, 43152980, 42069092, 45030937, 43273299, 51012083, 5316841, 63027345, 64016972, 5729081, 66039868, 71090162, 72049133, 78048433, 76040903, 76047105, 98032507, 13128889, 14030166, 14047879, 14183938, 17027720, 18077451, 23015696, 24015066, 25044546, 29086858, 38015253, 36011113, 38020266, 51009810, 51042239, 51055264, 5701921, 53103803, 5711545, 65013816, 65010086, 67191441, 71085775, 7448620, 70087962, 75005448, 66030080, 7748848, 76004645, 78059937, 85099964, 85128325, 67009440, 91123130, 1023133, 14109356, 23305528, 23208480, 23227648, 23232835, 37051796, 37052455, 41011530, 41039973, 435019, 48037848, 42069304, 43252773, 51054577, 61076923, 62071780, 62176079, 76047057, 77046331, 7988518, 91146971, 1043477, 12064887, 13113338, 13134712, 14149761, 14046873, 14057836, 14160583, 15041541, 16148021, 15062091, 23048044, 23167227, 23332046, 23310298, 25034440, 37001835, 43254697, 55072254, 63029139, 65025665, 66004052, 75017719, 76004039, 83150144, 13189534, 14118360, 19271083, 15069561, 23248120, 19086163, 29156865, 29160146, 38001137, 41022812, 49037674, 50053399, 51013585, 51042301, 51042433, 62078624, 65030611, 65030855, 66010919, 63010599, 63031581, 67226349, 76003846, 76017993, 76045798, 76045805, 91143193, 1010463, 14124784, 16162483, 24025295, 24052818, 41023199, 43124809, 43161701, 48042217, 51016484, 62076483, 66007048, 75015291, 75038833, 8834733, 96084294, 98009102, 13158411, 78081554, 164391, 23334593, 23034087, 38015246, 428289, 43213949, 19212657, 51011209, 51013517, 51013684, 51016145, 51030311, 51055568, 5602700, 51002480, 53126895, 61078239, 58060147, 62165318, 67155729, 67222593, 65028942, 65036120, 72048212, 76002905, 76008109, 76043602, 76045427, 13128185, 13177227, 92072736, 14041380, 16191716, 22028046, 18096591, 23062357, 23155590, 23189763, 23252313, 28109945, 37041778, 956500, 43131106, 51034095, 51029613, 62160670, 65030752, 71086469, 76006788, 76038542, 76045910, 7525817, 91158198, 67196243, 12021802, 14141697, 22068408, 23157933, 24026626, 42076719, 48039186, 51013772, 51040756, 51040969, 51041541, 53135500, 62073509, 65002721, 65011480, 69004694, 67202355, 67212013, 67230683, 72048243, 77017154, 65029041, 65029930, 96101506, 65033385, 14161820, 15074897, 15078037, 14179257, 19171607, 19249467, 212336, 65036569, 29174029, 37057202, 37058847, 50042376, 5724073, 51034091, 62092910, 65013871, 65028962, 72049201, 7452336, 67248196, 70103073, 76036940, 14149052, 78061330, 78063486, 78076618, 51048239, 91155515, 958189, 98010756, 13148043, 14138851, 15066077, 17032884, 23239764, 24039538, 23055729, 23338933, 25043784, 29073727, 41002401, 51001458, 51040679, 5600711, 5704064, 62138422, 65033880, 63029219, 65010093, 65010213, 66034867, 67178994, 67215250, 75017698, 76005151, 76022015, 76038735, 76040827, 76043490, 824299, 91018258, 98033196, 98041080, 14023038, 14026239, 19105867, 16027075, 16155057, 2111393, 29173571, 37058071, 41000778, 41021439, 43318799, 43212761, 43094106, 51030241, 51042366, 51064249, 64006884, 62082876, 62115587, 65030108, 76040818, 76037511, 76037814, 13162894, 14127765, 14187034, 19202493, 23119474, 23127918, 23134373, 24047039, 29103499, 38000743, 42017125, 42077367, 51010139, 51013561, 51016020, 51016155, 51055232, 51056501, 51064204, 5666846, 5709400, 62124616, 655339, 66037327, 65026328, 65030472, 19168591, 78062580, 85139141, 14168729, 23233238, 23020612, 23305496, 25017200, 37046962, 37053601, 38042613, 1509544, 16117697, 65029931, 67211688, 67219973, 65030430, 76039968, 71069151, 78016631, 78037285, 8435089, 12035475, 13109494, 14082414, 23305542, 41051527, 51013665, 51013744, 51016114, 51040604, 51042264, 48043877, 43004577, 43093161, 65037180, 64016164, 65011581, 65013762, 65028880, 65030602, 73100146, 75020102, 75039787, 76020776, 76040574, 76043648, 77028426, 80028857, 13109499, 98010529, 23062474, 23128152, 23128187, 33048390, 41005424, 43082012, 38020121, 43268672, 5610796, 53118828, 65030534, 66002457, 65025809, 66039832, 67245643, 67020818, 67102218, 75014979, 7746011, 76002517, 7747832, 76037396, 76046751, 76049719, 15016252, 15017437, 15078035, 19287282, 216403, 23189769, 23334185, 38032979, 36087082, 41039970, 48038324, 63027274, 58051817, 62055908, 62082847, 66032261, 65030756, 62123614, 67198217, 67213136, 7444926, 75018242, 71023386, 71030837, 80007074, 92025871, 13129255, 98034172, 14158693, 14008034, 21020485, 23028678, 24051715, 23056536, 23099116, 29127874, 37063971, 42079705, 49037765, 50036599, 51013474, 51042483, 53108992, 53124376, 5665520, 62079414, 62188177, 63010620, 65030625, 67179316, 67239803, 83121852, 12000732, 13103561, 13116656, 15004332, 14147954, 14150878, 19186025, 23325138, 23347969, 24003382, 23128132, 24047112, 23227502, 42069305, 41037669, 47055945, 50051111, 51047664, 5762924, 37058879, 37060865, 65010143, 65024933, 62164909, 71050997, 76019993, 76040824, 84121886, 78024460, 91119467, 67088670, 11001412, 13137118, 13161745, 14139153, 19189170, 19293151, 168138, 23002301, 23057595, 18096830, 23253924, 25034329, 43124622, 43328213, 48036223, 51031010, 51031112, 37057799, 67244415, 72048197, 76001271, 76033423, 66037317, 83114558, 67093539, 67196099, 91001148, 67211070, 12029993, 18101855, 19141535, 16157584, 23127728, 23167514, 23105316, 1016060, 37058449, 12001267, 43252195, 43339361, 51041947, 53104994, 48043581, 61073507, 51001052, 62093574, 51015896, 64017075, 65000028, 67187888, 71048713, 67226102, 72014282, 7524680, 76016011, 76022003, 91123109, 1019009, 1037884, 13116856, 133361, 15022986, 14089760, 14125784, 14131707, 23057700, 14036439, 23166404, 23253958, 37057995, 37064805, 41014724, 41020781, 51015430, 61069962, 65010223, 65010081, 66032260, 67212010, 67226083, 67033808, 75039574, 76038341, 77012416, 79026579, 86055025, 93089436, 8835309, 13104283, 16142385, 16155315, 16170637, 19265969, 23240155, 29128571, 33046739, 36005316, 51008472, 51008511, 51013519, 51013563, 51015785, 51016107, 51041059, 51055624, 5261774, 63027507, 65028823, 65029922, 67196046, 65030609, 66035259, 76040849, 76005134, 76039967, 76040551, 1042087, 13137229, 15071261, 19149208, 23062365, 37063762, 38037426, 39002041, 42071636, 42073902, 43008682, 41038377, 43155225, 48042243, 53028243, 51031109, 51032518, 51040660, 51047691, 5666422, 62160625, 63027258, 67029438, 66002963, 75000360, 67229157, 71030662, 76037048, 76020649, 8835457, 96101645, 91158071, 67029309, 23214131, 38037209, 51049138, 67018462, 14145896, 14160582, 18081030, 14027525, 2116244, 14077013, 51042403, 29179725, 98017556, 76049593, 53110134, 67177054, 19219253, 13161746, 15024084, 78062969, 14074340, 27110883, 24045245, 51054900, 14027535, 63024177, 91004706, 35026012, 37041575, 48032428, 13110358, 43061451, 78071881, 51015935, 14149684, 76049098, 78043557, 13153816, 16170637 )"
        testPlayers = pd.read_sql(testQuery, dbConnection)
        
        players = logic.FindSimilarPlayers()
        dbConnection.close();

        self.assertEqual(players.equals(testPlayers),True)

class TestFindPlayerWithSimilarAbilities(unittest.TestCase):
    
    def test_FindPlayerWithSimilarAbilities(self):
        alchemyEngine = create_engine(Settings.dbConString, pool_recycle=3600);
        dbConnection = alchemyEngine.connect();
        logic = Logic(dbConnection, 16170637)        
        targetAbilities = ['striker', 'rightfoot', 'heading', 'acceleration', 'pace', 'temperament', 'pressure', 'dribbling', 'composure', 'firsttouch', 'agility', 'sportsmanship', 'finishing', 'decisions', 'leadership', 'leftfoot', 'loyalty', 'professional', 'offtheball', 'technique']
        playersWithSimilarAbilities = Logic.FindPlayersWithSimilarAbilities(logic,targetAbilities)
        self.assertIn([1036117],playersWithSimilarAbilities)
        self.assertIn([12034183],playersWithSimilarAbilities)
        self.assertIn([13129199],playersWithSimilarAbilities)
        self.assertIn([14026322],playersWithSimilarAbilities)
        self.assertIn([1509925],playersWithSimilarAbilities)
        self.assertIn([19190933],playersWithSimilarAbilities)
        
        dbConnection.close();


if __name__ == '__main__':
    unittest.main()