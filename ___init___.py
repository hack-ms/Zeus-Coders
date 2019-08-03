from getallfiles import GetAll
from pathlib import Path
from getScriptToList import GetScriptFromDBToList
from putListToDb import PutTxtIntoDBNotaGeral
import os, glob

def main(username, password):
    projectPath = os.path.dirname(os.path.realpath(__file__))
    #GetAll(path + "\\texto\\")
    #GetScriptFromDBToList(path)
    path = os.path.join(projectPath, "sqlserver.config")
    sqlConfig = open(path).read()
    
    for file in os.listdir(projectPath + "\\texto"):
        if file.endswith(".txt"):
            table = ''
            if "caracteristicas" in file:
                table="CaracteristicaEscola"
            elif "matriculas-consolidadas" in file:
                table="MatriculaConsolidada"
            elif "matriculas-por-idade" in file:
                table="MatriculaIdade"
            elif "notas-gerais" in file:
                table="NotaGeral"
            elif "notas-por-dimensao" in file:
                table="NotaDimensao"
            else:
                table="PerfilRespondente"
                
            path = projectPath + "\\texto\\" + file
            PutTxtIntoDBNotaGeral(sqlConfig, path, table)

    
   
if __name__ == "__main__":
    username = "lupadocidadao"
    password = "esaniagro12"
    main(username, password)