import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 20, 30])
y1 = np.array([20, 40, 10])
y2 = np.array([40, 10, 30])

plt.plot(x, y1, color='blue', linestyle=':', linewidth=2, label='line1-dotted')
plt.plot(x, y2, color='red', linestyle='--', linewidth=4, label='line2-dashed')

plt.title('Plot with two or more lines with different styles')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()

plt.xlim(10, 30)
plt.ylim(10, 40)

plt.show()
#