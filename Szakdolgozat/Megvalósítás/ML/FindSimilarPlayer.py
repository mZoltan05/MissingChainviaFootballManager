from sqlalchemy import create_engine
import sys
from Logic import Logic
from settings import Settings
from sklearn.preprocessing import StandardScaler



def main(id):
    
    alchemyEngine = create_engine(Settings.dbConString, pool_recycle=3600);
    dbConnection = alchemyEngine.connect();

    logic = Logic(dbConnection,int(id))
    players = logic.FindSimilarPlayers()
    
    dbConnection.close();

    playerid = players['playerid']
    players_withoutid = players.drop(columns = ['playerid'])
    players_withoutid = StandardScaler().fit_transform(players_withoutid)

    k = logic.DetermineTheOptimalKValue(players_withoutid)

    print(logic.FindPlayersToReturn(players_withoutid,playerid, k),end="")
    



if __name__ == "__main__":
    main(sys.argv[1])
