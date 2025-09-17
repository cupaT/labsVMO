import matplotlib.pyplot as plt
import numpy as np

def y(x):
    return x * x - x - 6

x = np.linspace(-3, 5, 400)
y_vals = y(x)

plt.plot(x, y_vals, label='y(x) = x*x - x - 6', color='blue')
plt.axhline(0, color='black', linewidth=1)

roots = [3, -2]
plt.scatter(roots, [0, 0], color='red', zorder=5, label='Корни уравнения')

plt.title('График функции y(x) = x*x - x - 6')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.xlim(-3, 5)
plt.ylim(-10, 10)
plt.show()