from sqlalchemy import create_engine
import sys
from Logic import Logic
from settings import Settings
from sklearn.preprocessing import StandardScaler



def main(pos):
    
    alchemyEngine = create_engine(Settings.dbConString, pool_recycle=3600);
    dbConnection = alchemyEngine.connect();

    logic = Logic(dbConnection,pos)
    players = logic.GetUnderratedPlayers()
    
    dbConnection.close();

    print(players,end="")
    



if __name__ == "__main__":
    main(sys.argv[1])
