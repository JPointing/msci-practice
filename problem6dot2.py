import numpy as np
import matplotlib.pyplot as plt
x,y = np.loadtxt('xy.txt', delimiter='\t', dtype=None, unpack=True)

print x[0:10]

plt.plot(x, y)

plt.show()
