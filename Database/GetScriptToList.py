import os
from Database.GetListFromDatabase import GetRowsFromDB

def GetScriptFromDBToList(projectPath, sqlScript):
    path = os.path.join(projectPath, "sqlserver.config")
    sqlConfig = open(path).read()
    
    #path = projectPath + "\\SqlScripts\\ScriptIndiceReprovacao.sql"
    path = projectPath + "\\SqlScripts\\" + sqlScript
    listProp = GetRowsFromDB(sqlConfig, path)
    
    return listProp
    