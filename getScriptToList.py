import os
import sys
from getlistfromdb import GetRowsFromDB

def GetScriptFromDBToList(projectPath):
    path = os.path.join(projectPath, "sqlserver.config")
    sqlConfig = open(path).read()
    
    path = projectPath + "\\SqlScripts\\ScriptIndiceReprovacao.sql"
    listProp = GetRowsFromDB(sqlConfig, path)
    sys.stdout.write("\nTotal de coordenadas = " + str(len(listProp)) + "\n\n")
    return listProp
    