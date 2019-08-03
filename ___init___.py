from getallfiles import GetAllFiles
from pathlib import Path
from getScriptToList import GetScriptFromDBToList
from putListToDb import PutTxtIntoDBNotaGeral
import os, glob

def importoToDb(projectPath):
    path = os.path.join(projectPath, "sqlserver.config")
    sqlConfig = open(path).read()
    
    files = os.listdir(projectPath + "\\texto")

    for file in files:
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

            textPath = projectPath + "\\texto\\"
            path = projectPath + "\\texto\\" + file
            
            if 'IMPORTADO' not in path:
                PutTxtIntoDBNotaGeral(sqlConfig, textPath, file, table)

def main(username, password):
    # Passo 1 - Baixar arquivos
    projectPath = os.path.dirname(os.path.realpath(__file__))
    GetAllFiles(projectPath + "\\texto\\")
    
    # Passo 2 - Importar arquivos para banco de dados
    importoToDb(projectPath)

    # Passo 3 - Consulta dados no banco de dados
    #GetScriptFromDBToList(projectPath)

    # Passo 4 - Plotar gráfico conforme a consulta

    # Passo 5 - Postar na rede social
    

  
if __name__ == "__main__":
    username = "lupadocidadao"
    password = "esaniagro12"
    main(username, password)