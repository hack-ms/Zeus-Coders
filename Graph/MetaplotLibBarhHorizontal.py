import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import datetime

today = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

def PlotGraphIndeceDeReprovacaoMunicipio(projectPath, result):
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Example data
    municipio = []
    performance = []
    for item in result:
        municipio.append(item.NomeMunicipio)
        performance.append(item.PorcentagemReprovados)

    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(municipio))
    error = np.random.rand(len(municipio))
    ax.set_xlabel('porcentagem(%)')
    ax.set_title('Municípios com maior indece de reprovação')
    ax.barh(y_pos, performance, xerr=error, align='center', color='red')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(municipio, rotation=48,fontsize=6)
    ax.invert_yaxis()  # labels read top-to-bottom

    for i, v in enumerate(performance):
        ax.text(v + 1, i + .18, str(v) + ' %', color='red', fontweight='bold')
    
    imagem = projectPath + '\\Imagens\\IndeceReprovacaoMunicipio_'+today+'.jpg'
    plt.savefig(imagem)

    return imagem

def PlotGraphIndeceDeEvasaoEscolarMunicipio(projectPath, result):
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Example data
    municipio = []
    performance = []
    for item in result:
        municipio.append(item.NomeMunicipio)
        performance.append(item.Porcentagem)

    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(municipio))
    error = np.random.rand(len(municipio))
    ax.set_xlabel('porcentagem(%)')
    ax.set_title('Municípios com maior indece de Evasão')
    ax.barh(y_pos, performance, xerr=error, align='center', color='red')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(municipio, rotation=48,fontsize=6)
    ax.invert_yaxis()  # labels read top-to-bottom

    for i, v in enumerate(performance):
        ax.text(v + 1, i + .18, str(v) + ' %', color='red', fontweight='bold')
    
    imagem = projectPath + '\\Imagens\\IndeceEvasaoMunicipio_'+today+'.jpg'
    plt.savefig(imagem)

    return imagem

def PlotGraphIndeceDeAprovacaoMunicipio(projectPath, result):
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Example data
    municipio = []
    performance = []
    for item in result:
        municipio.append(item.NomeMunicipio)
        performance.append(item.Porcentagem)

    plt.rcdefaults()
    fig, ax = plt.subplots()  
    y_pos = np.arange(len(municipio))
    error = np.random.rand(len(municipio))
    ax.set_xlabel('porcentagem(%)')
    ax.set_title('Municípios com maior indece de aprovação')
    ax.barh(y_pos, performance, xerr=error, align='center', color='blue')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(municipio, rotation=48,fontsize=6)
    ax.invert_yaxis()  # labels read top-to-bottom

    for i, v in enumerate(performance):
        ax.text(v + 1, i + .18, str(v) + ' %', color='blue', fontweight='bold')
    
    imagem = projectPath + '\\Imagens\\IndeceAprovacaoMunicipio_'+today+'.jpg'
    plt.savefig(imagem)

    return imagem