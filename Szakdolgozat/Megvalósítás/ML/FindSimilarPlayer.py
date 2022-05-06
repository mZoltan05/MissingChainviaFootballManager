import pandas as pd
from sqlalchemy import create_engine
import sys
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans



alchemyEngine   = create_engine('postgresql+psycopg2://postgres:e13Jpgmzc@127.0.0.1/PlayerStats', pool_recycle=3600);
dbConnection = alchemyEngine.connect();


def FindSimilarPlayers(id):

    targetAbilities = FindTargetAbilities(id)
    playersWithSimilarAbilities = FindPlayersWithSimilarAbilities(targetAbilities)

    playersQuery = "SELECT playerid, "
    for j in range(len(targetAbilities)-1):
        playersQuery += targetAbilities[j] + ", "
    playersQuery += targetAbilities[-1] + " FROM score_bak WHERE playerid IN ( "
    for j in range(len(playersWithSimilarAbilities)):
        playersQuery += str(playersWithSimilarAbilities[j][0]) + ", "
    playersQuery += str(id) + " ) "

    players = pd.read_sql(playersQuery, dbConnection)
    return players

def FindTargetAbilities(id):

    targetAbilitiesQuery = """SELECT colname FROM (
                                SELECT
                                   unnest(array['aerialability', 'commandofarea', 'communication', 'eccentricity', 'handling', 'kicking', 'oneonones', 'reflexes', 'rushingout', 'tendencytopunch', 'throwing', 'corners', 'crossing', 'dribbling', 'finishing', 'firsttouch', 'freekicks', 'heading', 'longshots', 'longthrows', 'marking', 'passing', 'penaltytaking', 'tackling', 'technique', 'aggression', 'anticipation', 'bravery', 'composure', 'concentration', 'vision', 'decisions', 'determination', 'flair', 'leadership', 'offtheball', 'positioning', 'teamwork', 'workrate', 'acceleration', 'agility', 'balance', 'jumping', 'leftfoot', 'naturalfitness', 'pace', 'rightfoot', 'stamina', 'strength', 'consistency', 'dirtiness', 'importantmatches', 'injuryproness', 'versatility', 'adaptability', 'ambition', 'loyalty', 'pressure', 'professional', 'sportsmanship', 'temperament', 'controversy', 'goalkeeper', 'sweeper', 'striker', 'attackingmidcentral', 'attackingmidleft', 'attackingmidright', 'defendercentral', 'defenderleft', 'defenderright', 'defensivemidfielder', 'midfieldercentral', 'midfielderleft', 'midfielderright', 'wingbackleft', 'wingbackright']) AS colname,
                                   unnest(array[aerialability, commandofarea, communication, eccentricity, handling, kicking, oneonones, reflexes, rushingout, tendencytopunch, throwing, corners, crossing, dribbling, finishing, firsttouch, freekicks, heading, longshots, longthrows, marking, passing, penaltytaking, tackling, technique, aggression, anticipation, bravery, composure, concentration, vision, decisions, determination, flair, leadership, offtheball, positioning, teamwork, workrate, acceleration, agility, balance, jumping, leftfoot, naturalfitness, pace, rightfoot, stamina, strength, consistency, dirtiness, importantmatches, injuryproness, versatility, adaptability, ambition, loyalty, pressure, professional, sportsmanship, temperament, controversy, goalkeeper, sweeper, striker, attackingmidcentral, attackingmidleft, attackingmidright, defendercentral, defenderleft, defenderright, defensivemidfielder, midfieldercentral, midfielderleft, midfielderright, wingbackleft, wingbackright]) AS scores
                                FROM score_bak
                            WHERE scoreid = """ +str(id)+ """
                            ) AS p
                        ORDER BY p.scores DESC
                        LIMIT 20"""
    targetAbilities  = pd.read_sql(targetAbilitiesQuery, dbConnection)
    targetAbilities = targetAbilities['colname'].tolist()
    return targetAbilities


def FindPlayersWithSimilarAbilities(targetAbilities):

    playersWithSimilarAbilities = []
    filteredPlayers = FilterPlayers(targetAbilities)
    for player in filteredPlayers:
        currentPlayerAbilities = FindTargetAbilities(player[0])
        if compareList(targetAbilities,currentPlayerAbilities):
            playersWithSimilarAbilities.append(player)
    return playersWithSimilarAbilities


def FilterPlayers(targetAbilities):

    filteredPlayersQuery = "SELECT scoreid FROM score_bak WHERE "
    for column in targetAbilities:
        filteredPlayersQuery += column + ' > 7 AND '
    filteredPlayersQuery += ' 1=1 '
    filteredPlayers = pd.read_sql(filteredPlayersQuery, dbConnection)
    filteredPlayers = filteredPlayers.values.tolist()
    return filteredPlayers


def compareList(l1,l2):

    numberOfCommonFields = len(set(l1).intersection(l2))
    if numberOfCommonFields > 13:
        return True


def DetermineTheOptimalKValue(players_withoutid):

    sil = []
    kmax = 10
    for k in range(2, kmax+1):
        kmeans = KMeans(n_clusters=k, random_state=0).fit(players_withoutid)
        labels = kmeans.labels_
        sil.append(silhouette_score(players_withoutid, labels, metric = 'euclidean'))

    return sil.index(max(sil))+2



def FindPlayersToReturn(players_withoutid, playerid, k, id):

    kmeans = KMeans(n_clusters=k, random_state=0).fit(players_withoutid)
    y_kmeans = kmeans.predict(players_withoutid)
    positionOfBasePlayer = playerid.values.tolist().index(int(id))
    clusterOfBasePlayer = y_kmeans[positionOfBasePlayer]

    playerid = np.delete(playerid.values, positionOfBasePlayer)
    y_kmeans = np.delete(y_kmeans, positionOfBasePlayer)


    foundedPlayers = []

    for i in range(len(y_kmeans)):
        if y_kmeans[i] == clusterOfBasePlayer:
            foundedPlayers.append(playerid[i])
    return foundedPlayers



def main(id):
    from sklearn.preprocessing import StandardScaler
    players = FindSimilarPlayers(id)
    dbConnection.close();

    playerid = players['playerid']
    players_withoutid = players.drop(columns = ['playerid'])
    players_withoutid = StandardScaler().fit_transform(players_withoutid)

    k = DetermineTheOptimalKValue(players_withoutid)

    print(FindPlayersToReturn(players_withoutid,playerid, k, id),end="")
    



if __name__ == "__main__":
    main(sys.argv[1])
