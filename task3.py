import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


rows = 10
columns = 10
table = []

for i in range(rows * columns):
    left = np.random.randint(0, 20, size=(5, 3))
    right = np.fliplr(left)
    sprite = np.concatenate((left, right), axis=1)
    table.append(sprite)

pico8_colors = ['#1D2B53', '#7E2553', '#008751', '#AB5236', '#5F574F',
                '#C2C3C7', '#FFF1E8', '#FF004D', '#FFA300', '#FFEC27',
                '#00E436', '#29ADFF', '#83769C', '#FF77A8', '#FFCCAA',
                '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF',
                '#FFFFFF'
                ]

cmap_pico8_colors = ListedColormap(pico8_colors)
fig, position = plt.subplots(rows, columns, figsize=(8, 8))

for i in range(rows):
    for j in range(columns):
        position[i, j].imshow(table[i * columns + j], cmap=cmap_pico8_colors, interpolation='nearest')
        position[i, j].axis('off')

plt.subplots_adjust(wspace=1, hspace=1)
plt.show()
