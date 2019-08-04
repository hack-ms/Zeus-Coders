import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

def PlotGraph(projectPath, result):
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
    ax.set_title('Indice de reprovação por município')
    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(municipio, rotation=25,fontsize=6)
    ax.invert_yaxis()  # labels read top-to-bottom

    for i, v in enumerate(performance):
        ax.text(v + 1, i + .25, str(v) + ' %', color='blue', fontweight='bold')

    #plt.show()
    plt.savefig(projectPath + '\\images\\testeImagem.jpg')
    # im = Image.open(projectPath + "\\images\\testeImagem.png")
    # bg = Image.new("RGB", im.size, (255,255,255))
    # bg.paste(im,im)
    # bg.save(projectPath + "\\images\\colors.jpg", quality=95)