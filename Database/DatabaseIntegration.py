
from Database import PutListToDatabase
import os

def ImportoToDb(projectPath):
    path = os.path.join(projectPath, "sqlserver.config")
    sqlConfig = open(path).read()
    
    files = os.listdir(projectPath + "\\CollectedData")

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

            textPath = projectPath + "\\CollectedData\\"
            path = projectPath + "\\CollectedData\\" + file
            
            if 'IMPORTADO' not in path:
                PutListToDatabase.PutTxtIntoDBNotaGeral(sqlConfig, textPath, file, table)
