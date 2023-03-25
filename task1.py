import numpy as np
import matplotlib.pyplot as plt


left = np.random.randint(0, 2, size=(5, 3))
right = np.fliplr(left)
sprite = np.concatenate((left, right), axis=1)


plt.imshow(sprite, cmap='binary', interpolation='nearest')
plt.show()
