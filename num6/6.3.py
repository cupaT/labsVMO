import matplotlib.pyplot as plt

x = list(range(101))
y = [2*i for i in x]
z = [i**2 for i in x]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))

ax1.plot(x, y, color='blue', linewidth=5)
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax2.plot(x, z, color='red', linewidth=5, linestyle='--')
ax2.set_xlabel('x')
ax2.set_ylabel('z')

plt.tight_layout()
plt.show()