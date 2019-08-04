import pyodbc
import os

def PutTxtIntoDBNotaGeral(sqlConfig, textPath, file, table):
    conn = pyodbc.connect(sqlConfig)
    cursor = conn.cursor()

    pathTxt = textPath + file
    data_file = open(pathTxt, encoding="utf8")
    txt = data_file.read()
    aux = txt.split("\n")
    itercars = iter(aux)
    next(itercars)
    j = 1
    data_file.close()

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
        os.rename(pathTxt, textPath + "IMPORTADO - " + file) 
    except:
        conn.rollback()
    