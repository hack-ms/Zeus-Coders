import pyodbc

def GetGeoLocationFromDB(sqlConfig, pathTxt, pathSql):
    conn = pyodbc.connect(sqlConfig)
    cursor = conn.cursor()
    
    data_file = open(pathTxt)
    txt = data_file.read()
    data_file.Close()

    data_file = open(pathSql)
    sqlText = data_file.read()
    data_file.Close()
    values = [line.split() for line in txt]
    cursor.executemany(sqlText, values)