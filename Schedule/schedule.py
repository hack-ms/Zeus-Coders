from Files import GetAllFiles
from Database import DatabaseIntegration
from Database.GetScriptToList import GetScriptFromDBToList
from pathlib import Path
from Graph import MetaplotLibBarhHorizontal
import glob
from integrations import instagram
import array as arr

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

    resultado = [] 
    #Escolas com maior indece de reprovação
    result = SelectDataFromDatabase(projectPath, "IndiceReprovacao.sql")
    imgIndeceReprovacao= MetaplotLibBarhHorizontal.PlotGraphIndeceDeReprovacaoMunicipio(projectPath, result)
    resultado.append({'imagem': imgIndeceReprovacao, 'caption':"Teste do post imgIndeceReprovacao"})

    result = SelectDataFromDatabase(projectPath, "IndiceAprovacao.sql")
    imgIndeceAprovacao= MetaplotLibBarhHorizontal.PlotGraphIndeceDeAprovacaoMunicipio(projectPath, result)
    resultado.append({'imagem': imgIndeceAprovacao, 'caption':"Teste do post imgIndeceAprovacao"})

    result = SelectDataFromDatabase(projectPath, "IndeceDeEvasaoEscolar.sql")
    imgIndeceEvasao= MetaplotLibBarhHorizontal.PlotGraphIndeceDeEvasaoEscolarMunicipio(projectPath, result)
    resultado.append({'imagem': imgIndeceEvasao, 'caption':"Teste do post imgIndeceEvasao"})

    return resultado

def PostSocialMidia(images):
    # Passo 5 - Postar na rede social
    instagram.post(images)


# def print_time(a='default'):
#     print("From print_time", time.time(), a)
