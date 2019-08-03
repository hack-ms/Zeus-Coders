import os
import sys
from getlistfromdb import GetRowsFromDB

def GetScriptFromDBToList():
    projectPath = dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(projectPath, "sqlserver.config")
    sqlConfig = open(path).read()
    
    path = projectPath + "\\SqlScripts\\ScriptEscolasComMaioresMenoresNotasPorMunicipio.sql"
    listProp = GetRowsFromDB(sqlConfig, path)
    sys.stdout.write("\nTotal de coordenadas = " + str(len(listProp)) + "\n\n")