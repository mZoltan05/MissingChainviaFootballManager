import sys
from sqlalchemy import create_engine
import pandas as pd


def execSQL(command):
    try:
        alchemyEngine = create_engine('postgresql+psycopg2://postgres:e13Jpgmzc@127.0.0.1/PlayerStats', pool_recycle=3600);
        dbConnection = alchemyEngine.connect();

        dbConnection.execute(command)
        dbConnection.close();
    except Exception as e:
        print(e)

def ImportCSV(path):
    try:
        df = pd.read_csv (path)
        return df
    except Exception as e:
        print (e)

def UpdateTables(path):
    try:
        newData = ImportCSV(path)
        player = newData['playerid','name','clubid','age','born','height','weight','bestpos','nation','preferredfoot','value','wage']
        score = newData.drop(columns = ['playerid','name','clubid','age','born','height','weight','bestpos','nation','preferredfoot','value','wage'])

        execSQL('SELECT * INTO PlayerTemp FROM Player')
        execSQL('TRUNCATE TABLE Player')
        execSQL('SELECT * INTO ScoreTemp FROM Score')
        execSQL('TRUNCATE TABLE Score')


        alchemyEngine = create_engine('postgresql+psycopg2://postgres:e13Jpgmzc@127.0.0.1/PlayerStats', pool_recycle=3600);
        dbConnection = alchemyEngine.connect();


        player.to_sql('Player', con=dbConnection, if_exists='replace',index=False)
        score.to_sql('Score', con=dbConnection, if_exists='replace',index=False)
        histdata = CreateHistData()
        if histdata == False or len(dbConnection.execute("SELECT * FROM Player").fetchall() != len(newData)) or len(dbConnection.execute("SELECT * FROM Score").fetchall() != len(newData)):
            execSQL('TRUNCATE TABLE Player')
            execSQL('TRUNCATE TABLE Score')
            execSQL('INERT INTO Player AS SELECT * FROM PlayerTemp')
            execSQL('INERT INTO Score AS SELECT * FROM ScoreTemp')
            execSQL('DROP TABLE ScoreTemp')
            execSQL('DROP TABLE PlayerTemp')
            dbConnection.close();
            return False
        execSQL('DROP TABLE ScoreTemp')
        execSQL('DROP TABLE PlayerTemp')
        dbConnection.close();
        return True


    except Exception as e:
        print(e)
        return False


def CreateHistData():
    try:
        execSQL('INSERT INTO Player_hist AS SELECT * FROM PlayerTemp')
        execSQL('INSERT INTO Score_hist AS SELECT * FROM ScoreTemp')
        execSQL('UDATE Player_hist SET ValidTo = CURRENT_DATE WHERE ValidTo IS NULL')
        execSQL('UDATE Score_hist SET ValidTo = CURRENT_DATE WHERE ValidTo IS NULL')
        return True
    except Exception as e:
        print(e)
        return False

def main(path):
    UpdateTables(path)


if __name__ == "__main__":
    main(sys.argv[1])