import pyodbc

def PutTxtIntoDBNotaGeral(sqlConfig, pathTxt, table):
    conn = pyodbc.connect(sqlConfig)
    cursor = conn.cursor()
    
    data_file = open(pathTxt, encoding="utf8")
    txt = data_file.read()
    aux = txt.split("\n")
    itercars = iter(aux)
    next(itercars)
    j = 1
    
    try:
        for row in itercars:
            if row != '':
                param = row.split(';')

                if "Nota" in table:
                    result = "('%s')" % "'| '".join(map(str, param))
                    result = result.replace('"','')
                    result = result.replace('•','')
                    restul = result.replace("""', '""", ",")
                    result = result.replace(",", ".")
                    result = result.replace("|", ",")
                else:
                    result = "('%s')" % "', '".join(map(str, param))

                sqlText = "INSERT INTO " + table + " VALUES " + result
                print("\n " + str(j) + " - " + sqlText)
                j += 1
                cursor.execute(sqlText)
        conn.commit()
    except:
        conn.commit()
    