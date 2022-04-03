"""
Numpy
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 20, 1000)

y1 = np.sin(x - np.cos(x)) * np.cos(x - np.sin(x))
y2 = np.cos(x)

plt.plot(x , y1, "-g", label="sine")
plt.plot(x , y2, "-b", label="cos")

plt.legend(loc="upper right")

plt.ylim(-5, 5)
plt.show()