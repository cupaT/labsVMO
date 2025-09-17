import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 50)
y = 3 * x

plt.plot(x, y, color='blue')
plt.title('Draw a line.')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.xlim(0, 50)
plt.ylim(0, 160)
plt.show()