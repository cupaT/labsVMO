import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([2, 4, 6, 8])
y1 = np.array([1, 6, 11, 20])

x2 = np.array([3, 5, 7, 9])
y2 = np.array([2, 10, 20, 22])

plt.scatter(x1, y1, color='blue', marker='*')
plt.scatter(x2, y2, color='red', marker='o', s=70)

plt.xlim(0, 10)
plt.ylim(0, 30)
plt.show()