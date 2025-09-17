import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4, 100)
y1 = 3 - x**2/5
y2 = 0.5 + 1.5 * np.sin(2*x)

np.random.seed(0)
scatter_x = np.random.uniform(0, 4, 50)
scatter_y = np.random.uniform(0.5, 3, 50)

fig, ax = plt.subplots(figsize=(8, 6))

ax.grid(which='major', color='gray', linestyle='--', linewidth=0.7)
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)

ax.set_xticks(np.arange(0, 5, 1), minor=False)
ax.set_yticks(np.arange(0, 5, 1), minor=False)

minor_xticks = np.arange(0, 4.25, 0.25)
ax.set_xticks(minor_xticks, minor=True)
ax.set_xticklabels(
    [f'{val:.2f}' if val not in np.arange(0, 5, 1) else '' for val in minor_xticks],
    minor=True
)

ax.set_yticks(np.arange(0, 4.25, 0.25), minor=True)

ax.plot(x, y1, color='blue', linewidth=2, label='Синяя линия')
ax.plot(x, y2, color='red', linewidth=2, label='Красная линия')

ax.scatter(scatter_x, scatter_y, s=50, facecolors='none', edgecolors='black', linewidths=1)

for spine in ax.spines.values():
    spine.set_linewidth(2)

ax.set_title('Элементы изображения')
ax.set_xlabel('OX')
ax.set_ylabel('OY')
ax.legend(loc='upper right')

plt.xlim(0, 3)
plt.ylim(0, 3)

plt.tight_layout()
plt.show()