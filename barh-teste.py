import matplotlib.pyplot as plt
import numpy as np
import getScriptToList as lst
from PIL import Image
import os, sys

# Fixing random state for reproducibility
np.random.seed(19680801)


lita = lst.GetScriptFromDBToList()

# Example data
municipio = []
performance = []

for item in lita:
    municipio.append(item.NomeMunicipio)
    performance.append(item.PorcentagemReprovados)

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(15, 5))

y_pos = np.arange(len(municipio))
error = np.random.rand(len(municipio))

ax.set_xlabel('porcentagem(%)')
ax.set_title('Indice de reprovação por município')
ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(municipio)
ax.invert_yaxis()  # labels read top-to-bottom

#plt.show()
plt.savefig('images/testeImagem.png')

im = Image.open("images/testeImagem.png")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im,im)
bg.save("images/colors.jpg")

