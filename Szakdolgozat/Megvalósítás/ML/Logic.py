import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

class Logic:
    
  
    def __init__(self, dbConnection, param):
        self.dbConnection = dbConnection
        if str(type(param))[8:-2] == 'int': 
            self.id = param
        else:
            self.pos = param
    
    def FindSimilarPlayers(self):

        targetAbilities = self.FindTargetAbilities(self.id)
        playersWithSimilarAbilities = self.FindPlayersWithSimilarAbilities(targetAbilities)

        playersQuery = "SELECT playerid, "
        for j in range(len(targetAbilities)-1):
            playersQuery += targetAbilities[j] + ", "
        playersQuery += targetAbilities[-1] + " FROM score_bak WHERE playerid IN ( "
        for j in range(len(playersWithSimilarAbilities)):
            playersQuery += str(playersWithSimilarAbilities[j][0]) + ", "
        playersQuery += str(self.id) + " ) "
        #print(playersQuery,"************************************************")
        players = pd.read_sql(playersQuery, self.dbConnection)
        return players


    def FindTargetAbilities(self, id):
        targetAbilitiesQuery = """SELECT colname FROM (
                                    SELECT
                                    unnest(array['aerialability', 'commandofarea', 'communication', 'eccentricity', 'handling', 'kicking', 'oneonones', 'reflexes', 'rushingout', 'tendencytopunch', 'throwing', 'corners', 'crossing', 'dribbling', 'finishing', 'firsttouch', 'freekicks', 'heading', 'longshots', 'longthrows', 'marking', 'passing', 'penaltytaking', 'tackling', 'technique', 'aggression', 'anticipation', 'bravery', 'composure', 'concentration', 'vision', 'decisions', 'determination', 'flair', 'leadership', 'offtheball', 'positioning', 'teamwork', 'workrate', 'acceleration', 'agility', 'balance', 'jumping', 'leftfoot', 'naturalfitness', 'pace', 'rightfoot', 'stamina', 'strength', 'consistency', 'dirtiness', 'importantmatches', 'injuryproness', 'versatility', 'adaptability', 'ambition', 'loyalty', 'pressure', 'professional', 'sportsmanship', 'temperament', 'controversy', 'goalkeeper', 'sweeper', 'striker', 'attackingmidcentral', 'attackingmidleft', 'attackingmidright', 'defendercentral', 'defenderleft', 'defenderright', 'defensivemidfielder', 'midfieldercentral', 'midfielderleft', 'midfielderright', 'wingbackleft', 'wingbackright']) AS colname,
                                    unnest(array[aerialability, commandofarea, communication, eccentricity, handling, kicking, oneonones, reflexes, rushingout, tendencytopunch, throwing, corners, crossing, dribbling, finishing, firsttouch, freekicks, heading, longshots, longthrows, marking, passing, penaltytaking, tackling, technique, aggression, anticipation, bravery, composure, concentration, vision, decisions, determination, flair, leadership, offtheball, positioning, teamwork, workrate, acceleration, agility, balance, jumping, leftfoot, naturalfitness, pace, rightfoot, stamina, strength, consistency, dirtiness, importantmatches, injuryproness, versatility, adaptability, ambition, loyalty, pressure, professional, sportsmanship, temperament, controversy, goalkeeper, sweeper, striker, attackingmidcentral, attackingmidleft, attackingmidright, defendercentral, defenderleft, defenderright, defensivemidfielder, midfieldercentral, midfielderleft, midfielderright, wingbackleft, wingbackright]) AS scores
                                    FROM score_bak
                                WHERE scoreid = """ +str(id)+ """
                                ) AS p
                            ORDER BY p.scores DESC
                            LIMIT 20"""
        targetAbilities  = pd.read_sql(targetAbilitiesQuery, self.dbConnection)
        targetAbilities = targetAbilities['colname'].tolist()
        return targetAbilities


    def FindPlayersWithSimilarAbilities(self, targetAbilities):
        playersWithSimilarAbilities = []
        filteredPlayers = self.FilterPlayers(targetAbilities)
        for player in filteredPlayers:
            currentPlayerAbilities = self.FindTargetAbilities(player[0])
            if self.compareList(targetAbilities,currentPlayerAbilities):
                playersWithSimilarAbilities.append(player)
        #print(playersWithSimilarAbilities)
        return playersWithSimilarAbilities


    def FilterPlayers(self,targetAbilities):

        filteredPlayersQuery = "SELECT scoreid FROM score_bak WHERE "
        for column in targetAbilities:
            filteredPlayersQuery += column + ' > 7 AND '
        filteredPlayersQuery += ' 1=1 '
        filteredPlayers = pd.read_sql(filteredPlayersQuery, self.dbConnection)
        filteredPlayers = filteredPlayers.values.tolist()
        return filteredPlayers


    def compareList(self, l1,l2):

        numberOfCommonFields = len(set(l1).intersection(l2))
        if numberOfCommonFields > 13:
            return True
        return False


    def DetermineTheOptimalKValue(self, players_withoutid):

        sil = []
        kmax = 10
        for k in range(2, kmax+1):
            kmeans = KMeans(n_clusters=k, random_state=0).fit(players_withoutid)
            labels = kmeans.labels_
            sil.append(silhouette_score(players_withoutid, labels, metric = 'euclidean'))

        return sil.index(max(sil))+2


    def FindPlayersToReturn(self, players_withoutid, playerid, k):

        kmeans = KMeans(n_clusters=k, random_state=0).fit(players_withoutid)
        y_kmeans = kmeans.predict(players_withoutid)
        positionOfBasePlayer = playerid.values.tolist().index(int(self.id))
        clusterOfBasePlayer = y_kmeans[positionOfBasePlayer]

        playerid = np.delete(playerid.values, positionOfBasePlayer)
        y_kmeans = np.delete(y_kmeans, positionOfBasePlayer)


        foundedPlayers = []

        for i in range(len(y_kmeans)):
            if y_kmeans[i] == clusterOfBasePlayer:
                foundedPlayers.append(playerid[i])
        return foundedPlayers

    def GetPlayersOnPosition(self):
        if self.pos == 'GK':
            features = 'aerialability, commandofarea, communication, eccentricity, handling, kicking, oneonones, reflexes, rushingout, tendencytopunch, throwing'
        else:
            features = 'corners, crossing, dribbling, finishing, firsttouch, freekicks, heading, longshots, longthrows, marking, passing, penaltytaking, tackling, technique, aggression, anticipation, bravery, composure, concentration, vision, decisions, determination, flair, leadership, offtheball, positioning, teamwork, workrate, acceleration, agility, balance, jumping, leftfoot, naturalfitness, pace, rightfoot, stamina, strength, consistency, dirtiness, importantmatches, injuryproness, versatility, adaptability, ambition, loyalty, pressure, professional, sportsmanship, temperament, controversy'
        playersOnPosition  = pd.read_sql("""
                                            
                                            SELECT 
                                                s.playerid ,  value,
                                                """ +features+ """
                                            FROM 
                                                (SELECT * FROM player WHERE value > 0 and bestpos LIKE '%%"""+self.pos+"""%%') p
                                            INNER JOIN 
                                                score_bak s
                                            ON p.score_id = s.playerid
                                            """, self.dbConnection)
        return playersOnPosition


    def GetUnderratedPlayers(self):
        players = self.GetPlayersOnPosition()
        playerIds = players['playerid']
        value = players['value']
        playersWithoutIdAndValue = players.drop(columns = ['playerid','value'])
        
        reg = linear_model.LinearRegression()
        reg.fit(playersWithoutIdAndValue,value)
        y = reg.predict(playersWithoutIdAndValue)
        
        ids = []
        diffs = []
        for i in range(len(y)):
            if y[i] > players.value[i]:
                ids.append(playerIds[i])
                diffs.append(round(y[i]-players.value[i]))
        underratedPlayers = {'PlayerId':ids,'Differences':diffs}
        return list(pd.DataFrame(underratedPlayers).sort_values(by=['Differences'],ascending=False).PlayerId.head(100))
    