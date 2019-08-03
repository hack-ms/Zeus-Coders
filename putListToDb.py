import pyodbc

def PutTxtIntoDBNotaGeral(sqlConfig, pathTxt, table):
    conn = pyodbc.connect(sqlConfig)
    cursor = conn.cursor()
    
    data_file = open(pathTxt, encoding="utf8")
    txt = data_file.read()
    aux = txt.split("\n")
    itercars = iter(aux)
    next(itercars)

    try:
        for row in itercars:
            if row != '':
                param = row.split(';')
                i = 0
                while i < len(param):
                    try:
                        float(param[i])
                        i +=1
                    except ValueError:
                        print ("Not a float")
                        i +=1
                #data_file.Close()
                #values = [line.split() for line in txt]
                result = "('%s')" % "'| '".join(map(str, param))
                result = result.replace('"','')
                result = result.replace('•','')
                #result = result.replace(",", ".")
                result = result.replace("|", ",")
                sqlText = "INSERT INTO " + table + " VALUES " + result
                cursor.execute(sqlText)
        conn.commit()
    except:
        conn.commit()
    