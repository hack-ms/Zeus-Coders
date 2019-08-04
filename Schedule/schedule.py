from Files import GetAllFiles
from Database import DatabaseIntegration
from Database.GetScriptToList import GetScriptFromDBToList
from pathlib import Path
from Graph import MetaplotLibBarhHorizontal
import glob
from integrations import instagram
from integrations import faceboock
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
    resultado.append({'imagem': imgIndeceReprovacao, 'caption':"CIDADÃO VENHA FISCALIZAR CONOSCO: \nVocê está satisfeito com o índice de repovação escolar do seu município? Deixe abaixo o seu comentário, o Estado precisa saber da sua opinião. Conheça mais acessando o site: http://www.transparencia.ms.gov.br para saber mais sobre as escolas do seu município."})

    result = SelectDataFromDatabase(projectPath, "IndiceAprovacao.sql")
    imgIndeceAprovacao= MetaplotLibBarhHorizontal.PlotGraphIndeceDeAprovacaoMunicipio(projectPath, result)
    resultado.append({'imagem': imgIndeceAprovacao, 'caption':"CIDADÃO VENHA FISCALIZAR CONOSCO: \nVocê está satisfeito com o índice de aprovação escolar do seu município? Deixe abaixo o seu comentário, o Estado precisa saber da sua opinião. Conheça mais acessando o site: http://www.transparencia.ms.gov.br para saber mais sobre as escolas do seu município."})

    result = SelectDataFromDatabase(projectPath, "IndeceDeEvasaoEscolar.sql")
    imgIndeceEvasao= MetaplotLibBarhHorizontal.PlotGraphIndeceDeEvasaoEscolarMunicipio(projectPath, result)
    resultado.append({'imagem': imgIndeceEvasao, 'caption':"CIDADÃO VENHA FISCALIZAR CONOSCO: \nVocê está satisfeito com o índice de evasão escolar do seu município? Deixe abaixo o seu comentário, o Estado precisa saber da sua opinião. Conheça mais acessando o site: http://www.transparencia.ms.gov.br para saber mais sobre as escolas do seu município."})

    return resultado

def PostSocialMidia(images):
    # Passo 5 - Postar na rede social
    #instagram.post(images)
    faceboock.post(images)
