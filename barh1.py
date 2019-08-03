import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy as np

x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=3, sharex=True, figsize=(3, 5))


#grafico 01
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]
axs[0].set_title('blue should be up')
axs[0].plot(meses, valores)

#grafico 02
axs[1].set_title('blue should be down')
axs[1].imshow(x, origin='lower', interpolation=interp)

#grafico 03
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

rects1 = axs[2].bar(x - width/2, men_means, width, label='Men')
rects2 = axs[2].bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
axs[2].set_ylabel('Scores')
axs[2].set_title('Scores by group and gender')
axs[2].set_xticks(x)
axs[2].set_xticklabels(labels)
axs[2].legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        axs[2].annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

#plt.savefig('images/books_read.jpg')

plt.show()

