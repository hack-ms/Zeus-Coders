from Files import GetAllFiles
from Database import DatabaseIntegration
from Database.GetScriptToList import GetScriptFromDBToList
from pathlib import Path
from Graph import MetaplotLibBarh
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

def PlotGraph(projectPath, result):
    # Passo 4 - Plotar gráfico conforme a consulta
    MetaplotLibBarh.PlotGraph(projectPath, result)

def PostSocialMidia():
    # Passo 5 - Postar na rede social
    socialMidia = ""


# def print_time(a='default'):
#     print("From print_time", time.time(), a)
