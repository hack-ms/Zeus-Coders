from Files import GetAllFiles
from Database import DatabaseIntegration
from Database.GetScriptToList import GetScriptFromDBToList
from pathlib import Path
from Graph import MetaplotLibBarhHorizontal
import glob

# Passo 1 - Baixar arquivos
def ExtractData(projectPath):
    GetAllFiles.GetAllFilesOnWebsite(projectPath + "\\CollectedData\\")

# Passo 2 - Importar arquivos para banco de dados
def ImportTxtToDatabase(projectPath):
    DatabaseIntegration.ImportoToDb(projectPath)
    
def SelectDataFromDatabase(projectPath, sqlScript):
    # Passo 3 - Consulta dados no banco de dados
    return GetScriptFromDBToList(projectPath, sqlScript)

def PlotGraph(projectPath):
    # Passo 4 - Plotar gráfico conforme a consulta
 
    #Escolas com maior indece de reprovação
    result = SelectDataFromDatabase(projectPath, "IndiceReprovacao.sql")
    imgIndeceReprovacao= MetaplotLibBarhHorizontal.PlotGraphIndeceDeReprovacaoMunicipio(projectPath, result)

    result = SelectDataFromDatabase(projectPath, "IndiceAprovacao.sql")
    imgIndeceAeprovacao= MetaplotLibBarhHorizontal.PlotGraphIndeceDeAprovacaoMunicipio(projectPath, result)

    result = SelectDataFromDatabase(projectPath, "IndeceDeEvasaoEscolar.sql")
    imgIndeceAeprovacao= MetaplotLibBarhHorizontal.PlotGraphIndeceDeEvasaoEscolarMunicipio(projectPath, result)


def PostSocialMidia():
    # Passo 5 - Postar na rede social
    socialMidia = ""


# def print_time(a='default'):
#     print("From print_time", time.time(), a)
