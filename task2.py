import numpy as np
import matplotlib.pyplot as plt

rows = 20
columns = 20
table = []

for i in range(rows * columns):
    left_half = np.random.randint(0, 2, size=(5, 3))
    right_half = np.fliplr(left_half)
    sprite = np.concatenate((left_half, right_half), axis=1)
    table.append(sprite)


fig, position = plt.subplots(rows, columns, figsize=(8, 8))

for i in range(rows):
    for j in range(columns):
        position[i, j].imshow(table[i * columns + j], cmap='binary', interpolation='nearest')
        position[i, j].axis('off')

plt.subplots_adjust(wspace=1, hspace=1)
plt.show()
