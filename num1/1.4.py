import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 4, 5, 6, 7])
y = np.array([2, 6, 3, 6, 3])

plt.plot(x, y, 'r:', marker='o', markersize=10, markerfacecolor='blue')
plt.title('Display marker')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.xlim(1, 8)
plt.ylim(1, 8)
plt.show()